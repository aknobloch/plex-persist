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

def get_total_songs(music_collection) :

    total = 0

    for artist in music_collection.searchArtists():
        for track in artist.tracks():
            total += 1

    return total

def process_song(song) :

    writer = get_writer(song)

    if writer is None:
        return
    
    try :
        writer.write_song_info_to_disk()
    except Exception :
        log.exception('Error writing some, or all, of the song info to disk!')
        do_abort_prompt()

args = get_arg_parser().parse_args()

if args.debug:
    log.enable_debug()

username = args.username
password = args.password
server_name = args.server_name
section_name = args.section_name

account = MyPlexAccount(username, password)
plex = account.resource(server_name).connect()
music = plex.library.section(section_name)

total_songs = get_total_songs(music)
log.info('Found ' + str(total_songs) + ' total songs in collection.')

processed_songs = 0

for artist in music.searchArtists():
    for track in artist.tracks():

        processed_songs += 1
        song = Song(track)

        log.debug('-------------------')
        log.info('Processing song ' + str(processed_songs) + '/' + str(total_songs))
        log.debug('-------------------')
        log.debug(song)

        process_song(song)