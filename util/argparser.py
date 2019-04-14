import argparse

def get_arg_parser() :

    parser = argparse.ArgumentParser(
        prog='Plex Persist',
        usage='python3 persist.py MyServer Music aknobloch MY_P455W0RD',
        description='Persists the metadata information from a Plex Media Server.')

    parser.add_argument(
        'server_name',
        metavar='server',
        type=str,
        help='Name of the Plex server. This can be found by logging into \
                    the desired server via the Web UI. The name will be in the upper left.')

    parser.add_argument(
        'section_name',
        metavar='section',
        type=str,
        help='Name of the audio library section. This is usually \"Music\," \
                    but you may have renamed it during creation. You can find this \
                    by logging into the desired server via the Web UI. The names of \
                    your libraries will be on the left panel.')

    parser.add_argument(
        'username',
        metavar='username',
        type=str,
        help='Username for the owner of the Plex server.')

    parser.add_argument(
        'password',
        metavar='password',
        type=str,
        help='Password for the owner of the Plex server.')

    parser.add_argument(
        '--verbose',
        '-v',
        action='store_true',
        help='Enables verbose logging.',
        dest='debug')

    return parser