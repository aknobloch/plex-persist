import argparse
import urllib
import sys
from util.logutil import log
from logging import exception as log_exception
from plexapi.myplex import MyPlexAccount
from model.song import Song
from controller.writer import get_writer
from model.constants import FileType

if __name__ != '__main__':

    log.error('Plex Persist not called directly, exiting...')
    sys.exit()

parser = argparse.ArgumentParser(
    prog='Plex Persist',
    usage='python3 persist.py MyServer Music aknobloch MY_P455W0RD',
    description='Persists the metadata information from a Plex Media Server.'
)

parser.add_argument(
    'server_name',
    metavar='server',
    type=str,
    help='Name of the Plex server. This can be found by logging into \
                the desired server via the Web UI. The name will be in the upper left.')

parser.add_argument(
    'section_name',
    metavar='section',
    type=str,
    help='Name of the audio library section. This is usually \"Music\," \
                but you may have renamed it during creation. You can find this \
                by logging into the desired server via the Web UI. The names of \
                your libraries will be on the left panel.')

parser.add_argument(
    'username',
    metavar='username',
    type=str,
    help='Username for the owner of the Plex server.')

parser.add_argument(
    'password',
    metavar='password',
    type=str,
    help='Password for the owner of the Plex server.')

parser.add_argument(
    '--verbose',
    '-v',
    action='store_true',
    help='Enables verbose logging.',
    dest='debug')

args = parser.parse_args()

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

def process_song(song) :

    writer = get_writer(song)

    if writer is None:
        return
    
    try :
        writer.write_song_info_to_disk()
    except Exception :
        log.exception('Error writing some, or all, of the song info to disk!')
        do_abort_prompt()

def do_abort_prompt() :

    abort = ''

    while abort != 'Y' or abort != 'N' :
        abort = raw_input('Would you like to abort the process now? (y/n): ')
    
    if abort = 'Y' :
        sys.exit()

def get_total_songs(music_collection) :

    total = 0

    for artist in music_collection.searchArtists():
        for track in artist.tracks():
            total += 1

    return total