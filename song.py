from plexapi.audio import Track

class Song() :

    def __init__(self, track):

        self.title = self.__get_tag(track.title)
        self.artist = self.__get_tag(track.grandparentTitle)
        self.album = self.__get_tag(track.parentTitle)
        self.artwork_url = self.__get_artwork_url(track)

        abs_file_location = track.media[0].parts[0].file
        self.sys_location = self.__get_tag(abs_file_location)
        self.filetype = self.__get_tag(abs_file_location[abs_file_location.rfind('.') + 1:].upper())

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

    def __str__(self) :

        NEWLINE = '\n'
        return 'Title: ' + (self.title if self.title is not None else '[Unknown]') + NEWLINE \
        + 'Artist: ' + (self.artist if self.artist is not None else '[Unknown]') + NEWLINE \
        + 'Album: ' + (self.album if self.album is not None else '[Unknown]') + NEWLINE \
        + 'Artwork URL: ' + (self.artwork_url if self.artwork_url is not None else '[Unknown]') + NEWLINE \
        + 'File Location: ' + (self.sys_location if self.sys_location is not None else '[Unknown]') + NEWLINE \
        + 'Filetype: ' + (self.filetype if self.filetype is not None else '[Unknown]') + NEWLINE
