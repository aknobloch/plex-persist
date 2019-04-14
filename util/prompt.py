def do_abort_prompt() :

    abort = ''

    while abort != 'Y' or abort != 'N' :
        abort = raw_input('Would you like to abort the process now? (y/n): ')
    
    if abort == 'Y' :
        sys.exit()