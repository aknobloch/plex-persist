import sys
from util.logutil import log

def do_abort_prompt() :

    abort = ''

    while abort != 'Y' and abort != 'N' :
        abort = input('Would you like to abort the process now? (y/n): ').upper()

    if abort == 'Y' :
        log.info('Exiting...')
        sys.exit()