class FileType() :

    WAV = 'WAV'
    XWAV = 'X-WAV'

    FLAC = 'FLAC'
    XFLAC = 'X-FLAC'

    MPEG = 'MPEG'

    MP4 = 'MP4'

class TextStyle() :

    RED   = '\033[1;31m'  
    BLUE  = '\033[1;34m'
    CYAN  = '\033[1;36m'
    GREEN = '\033[0;32m'
    RESET = '\033[0;0m'
    BOLD    = '\033[;1m'
    REVERSE = '\033[;7m'

class LogLevel() :

    INFO = 'INFO'
    DEBUG = 'DEBUG'