from plexapi.audio import Track

class Song() :

    def __init__(self, track):

        self.title = self.__get_tag__(track.title)
        self.artist = self.__get_tag__(track.grandparentTitle)        
        self.album = self.__get_tag__(track.parentTitle)
        self.artwork_url = self.__get_tag__(track.thumbUrl)

        abs_file_location = track.media[0].parts[0].file
        self.sys_location = self.__get_tag__(abs_file_location)
        self.filetype = self.__get_tag__(abs_file_location[abs_file_location.rfind('.') + 1:].upper())

    '''
    Checks if the given name is NoneType or if Plex
    has labeled the tag with '[Unknown <tag type>]'.
    If so, returns None. Otherwise, returns name.
    '''
    def __get_tag__(self, name) :

        if name is None or name.strip().startswith('[Unknown') :
            return None
        else :
            return name

    def __str__(self) :

        NEWLINE = '\n'
        return 'Title: ' + (self.title if self.title is not None else '[Unknown]') + NEWLINE \
        + 'Artist: ' + (self.artist if self.artist is not None else '[Unknown]') + NEWLINE \
        + 'Album: ' + (self.album if self.album is not None else '[Unknown]') + NEWLINE \
        + 'Artwork URL: ' + (self.artwork_url if self.artwork_url is not None else '[Unknown]') + NEWLINE \
        + 'File Location: ' + (self.sys_location if self.sys_location is not None else '[Unknown]') + NEWLINE \
        + 'Filetype: ' + (self.filetype if self.filetype is not None else '[Unknown]') + NEWLINE
