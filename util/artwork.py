from urllib.request import urlretrieve
from util.logutil import log
from PIL import Image
import os

class AlbumArt() :

    def __init__(self, track_title, url) :

        self.temp_name = track_title + '_art_temp.png'
        self.resource_url = url

    def get_png_image_location(self) :

        image = Image.open(self.temp_name)
        image.thumbnail((600,600))
        image.save(self.temp_name)

        return self.temp_name

    def __enter__(self) :

        urlretrieve(self.resource_url, self.temp_name)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback) :

        if not os.path.isfile(self.temp_name) :
            log.debug('Temporary artwork file does not exist.')
            return

        try :
            os.remove(self.temp_name)
            log.debug('Temporary artwork image file deleted.')
        except OSError as e:
            log.error('Error deleting temporary artwork file located at ' + self.temp_name)

        
            