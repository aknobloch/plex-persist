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
        '-a',
        '--artist-filter',
        help='Optional filter for artist name. Only those matching the \
                    given filter query will be processed. This should be the \
                    artist name as seen in the Plex library.' ,
        dest='artist_filter')

    parser.add_argument(
        '--redis-server',
        help='Optional configuration specifying the host and port for a Redis \
                instance, to be used to track metadata changes. This should be \
                in the format of host:port, such as "192.168.0.1:4182". \
                Defaults to "localhost:6379".',
        dest='redis_server')

    parser.add_argument(
        '--redis-socket',
        help='Optional configuration specifying the socket for a Redis \
                instance, to be used to track metadata changes. This should be \
                in the format of a file location, such as "/tmp/redis.sock".',
        dest='redis_socket')

    parser.add_argument(
        '-d',
        '--dry-run',
        action='store_true',
        help='Outputs what information is retrieved without writing to disk.',
        dest='dry_run')

    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Enables verbose logging.',
        dest='debug')

    parser.add_argument(
        '--force-continue',
        action='store_true',
        help='Forces continue, even if errors occur.',
        dest='force_continue')

    return parser