from mutagen.flac import FLAC, Picture
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC, error, PictureType
from constants import FileType
from song import Song
from logutil import log
from artwork import AlbumArt

def get_writer(song) :

    if song.filetype == FileType.MPEG :
        return MPEGWriter(song)

    elif song.filetype == FileType.FLAC :
        return FLACWriter(song)

    else :

        log.error('Could not find appropriate tagger for ' + str(song.sys_location))
        return None

class AbstractSongWriter() :

    def __init__(self, song) :
        self.song = song

    def write_song_info_to_disk(self) :
        raise NotImplementedError("Class %s doesn't implement write_to_disk()" % (self.__class__.__name__))

class MPEGWriter(AbstractSongWriter) :

    def write_song_info_to_disk(self) :

        if self.song is None :
            return

        tags = EasyID3(self.song.sys_location)

        if self.song.title is not None: tags['title'] = self.song.title
        if self.song.artist is not None: tags['artist'] = self.song.artist
        if self.song.album is not None: tags['album'] = self.song.album

        tags.save()

        self.__add_album_art()

    def __add_album_art(self) :

        if self.song.artwork_url is None :

            log.debug('No album art found.')
            return

        with AlbumArt(self.song.title, self.song.artwork_url) as album_art :

            album_cover_data = open(album_art.get_png_image_location(), 'rb').read()

            tagger = ID3(self.song.sys_location)
            tagger.add(
                APIC(
                    encoding=3, # UTF-8
                    mime=u'image/png',
                    type=PictureType.COVER_FRONT,
                    desc=u'Cover',
                    data=album_cover_data
                )
            )

            tagger.save(v2_version=3)

class FLACWriter(AbstractSongWriter) :

    def write_song_info_to_disk(self) :
        
        tags = FLAC(self.song.sys_location)

        if self.song.title is not None: tags['title'] = self.song.title
        if self.song.artist is not None: tags['artist'] = self.song.artist
        if self.song.album is not None: tags['album'] = self.song.album

        tags.save()

        self.__add_album_art(tags)

    def __add_album_art(self, tags) :

        with AlbumArt(self.song.title, self.song.artwork_url) as album_art :

            album_cover_data = open(album_art.get_png_image_location(), 'rb').read()
            
            artwork = Picture()
            artwork.type = PictureType.COVER_FRONT
            artwork.mime = u'image/png'
            artwork.desc = u'Cover'
            artwork.data = album_cover_data

            tags.add_picture(artwork)
            tags.save()


