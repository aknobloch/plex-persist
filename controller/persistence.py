from model.song import Song
from util.logutil import log
from model.constants import FileIO

class SongPersistanceTracker:

    def __init__(self, server, song):
        self.server = server
        self.song = song
        
    def is_already_persisted(self):

        try:
            current_stored_hash = self.server.get_song_hash(self.song)

            if(current_stored_hash is None):
                return False

            current_stored_hash = current_stored_hash.decode(FileIO.ENCODING)
            return self.song.get_hash() == current_stored_hash

        except Exception:
            log.debug('Error checking hash - is server configured and available?')
            return False

    def mark_persisted(self):

        try:
            song_hash = self.song.get_hash()
            self.server.set_song_hash(self.song, song_hash)
        except Exception:
            log.debug('Error persisting hash - is server configured and available?')