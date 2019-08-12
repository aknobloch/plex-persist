import urllib
import sys
from util.argparser import get_arg_parser
from util.prompt import do_abort_prompt
from util.logutil import log
from logging import exception as log_exception
from plexapi.myplex import MyPlexAccount
from model.song import Song
from controller.writer import get_writer
from model.constants import FileType

if __name__ != '__main__':

    log.error('Plex Persist not called directly, exiting...')
    sys.exit()

def get_total_songs(music_collection, filter) :

    total = 0

    for artist in music_collection.searchArtists(title=filter):
        total += len(artist.tracks())

    return total

def process_song(song) :

    writer = get_writer(song)

    if writer is None:
        return
    
    try :
        writer.write_song_info_to_disk()
        pass
    except Exception :
        log.exception('Error writing some, or all, of the song info to disk!')
        do_abort_prompt()

args = get_arg_parser().parse_args()

if args.debug:
    log.enable_debug()

username = args.user
password = args.password
server_name = args.name
section_name = args.section
artist_filter = args.artist_filter
is_dry_run = args.dry_run

account = MyPlexAccount(username, password)
plex = account.resource(server_name).connect()
music = plex.library.section(section_name)

total_songs = get_total_songs(music, artist_filter)
log.info('Found ' + str(total_songs) + ' total songs in collection.')

if(artist_filter is not None and total_songs == 0) :
    log.error('The search parameter \'' + artist_filter + '\' yielded no results.')

processed_songs = 0

for artist in music.searchArtists(title=artist_filter):
    for track in artist.tracks():

        processed_songs += 1
        song = Song(track)

        if(is_dry_run or args.debug) :
            
            log.info('-------------------')
            log.info('Processing song ' + str(processed_songs) + '/' + str(total_songs))
            log.info('-------------------')
            log.info(song)

        # actually process the song only if NOT in dry-run mode
        if(is_dry_run is False) :

            process_song(song)

if(is_dry_run) :
    log.error('The above information was not written to disk, as Plex Persist was run in dry-run mode.')