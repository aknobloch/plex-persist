import argparse

def get_arg_parser() :

    parser = argparse.ArgumentParser(
        prog='Plex Persist',
        usage='python3 plex-persist.py --name uServer --section Music --user aknobloch --password MY_P455W0RD',
        description='Persists the metadata information from a Plex Media Server.')

    parser.add_argument(
        '-n',
        '--name',
        required=True,
        metavar='name',
        type=str,
        help='Name of the Plex server. This can be found by logging into \
                    the desired server via the Web UI. The name will be in the upper left.')

    parser.add_argument(
        '-s',
        '--section',
        required=True,
        metavar='section',
        type=str,
        help='Name of the audio library section. This is usually \"Music\," \
                    but you may have renamed it during creation. You can find this \
                    by logging into the desired server via the Web UI. The names of \
                    your libraries will be on the left panel.')

    parser.add_argument(
        '-u',
        '--user',
        required=True,
        metavar='username',
        type=str,
        help='Username for the owner of the Plex server.')

    parser.add_argument(
        '-p',
        '--password',
        required=True,
        metavar='password',
        type=str,
        help='Password for the owner of the Plex server.')

    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Enables verbose logging.',
        dest='debug')

    return parser