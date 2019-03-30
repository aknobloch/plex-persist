import magic
from logutil import log
from constants import FileType
from plexapi.audio import Track

class Song() :

    def __init__(self, track):
        
        self.title = self.__get_tag(track.title)
        self.artist = self.__get_tag(track.grandparentTitle)
        self.album = self.__get_tag(track.parentTitle)
        self.artwork_url = self.__get_artwork_url(track)

        abs_file_location = track.media[0].parts[0].file
        self.sys_location = self.__get_tag(abs_file_location)

        self.filetype = self.__get_filetype()

        log.debug('Created song reference:')
        log.debug(self)

    def __get_artwork_url(self, track) :
        
        if not self.is_empty(track.thumb) :
            return track.url(track.thumb)

        elif not self.is_empty(track.parentThumb) :
            return track.url(track.parentThumb)
            
        else :
            return self.__get_tag(track.url(track.grandparentThumb))

    '''
    Gets the tag name, or None if it is not tagged.
    '''
    def __get_tag(self, name) :

        if self.is_empty(name) :
            return None
        else :
            return name

    '''
    Checks if the given tag is NoneType or if Plex
    has labeled the tag with '[Unknown <tag type>]'.
    If so, returns true. Otherwise, returns false.
    '''
    def is_empty(self, tag) :

        return tag is None or tag.strip().startswith('[Unknown')

    def __get_filetype(self) :

        filetype = magic.from_file(self.sys_location, mime=True).upper()
        filetype = filetype[filetype.rfind('/') + 1:]

        if filetype == FileType.FLAC or filetype == FileType.XFLAC :
            return FileType.FLAC

        elif filetype == FileType.MP4 :
            return FileType.MP4

        elif filetype == FileType.MPEG :
            return FileType.MPEG

        elif filetype == FileType.WAV or filetype == FileType.XWAV :
            return FileType.WAV

        else :
            log.error('Could not find a valid filetype for the following path:')
            log.error(self.sys_location)
            return None

    def __str__(self) :

        NEWLINE = '\n'
        return 'Title: ' + (self.title if self.title is not None else '[Unknown]') + NEWLINE \
        + 'Artist: ' + (self.artist if self.artist is not None else '[Unknown]') + NEWLINE \
        + 'Album: ' + (self.album if self.album is not None else '[Unknown]') + NEWLINE \
        + 'Artwork URL: ' + (self.artwork_url if self.artwork_url is not None else '[Unknown]') + NEWLINE \
        + 'File Location: ' + (self.sys_location if self.sys_location is not None else '[Unknown]') + NEWLINE \
        + 'Filetype: ' + (self.filetype if self.filetype is not None else '[Unknown]') + NEWLINE
