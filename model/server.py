import redis
from model.song import Song
from util.logutil import log
from model.constants import App

class ServerInterface:
    def get_song_hash(self, song):
        raise NotImplementedError("Class %s doesn't implement get_song_hash()" % (self.__class__.__name__))

    def set_song_hash(self, song, hash_value):
        raise NotImplementedError("Class %s doesn't implement set_song_hash()" % (self.__class__.__name__))

class RedisServer(ServerInterface):

    def __init__(self, redis_server_location, redis_socket_location):

        if(redis_server_location is not None):
            redis_location = redis_server_location.split(':')
            self.server = redis.Redis(host=redis_location[0], port=redis_location[1])

        elif(redis_socket_location is not None):
            self.server = redis.Redis(unix_socket_path=redis_socket_location)

        else:
            log.info('Redis information not provided, defaulting to localhost.')
            self.server = redis.Redis()

    def get_song_hash(self, song):
        song_key = self.__get_song_key(song)
        return self.server.get(song_key)

    def set_song_hash(self, song, hash_value):
        song_key = self.__get_song_key(song)
        return self.server.set(song_key, hash_value)

    def __get_song_key(self, song):
        return App.NAME + song.sys_location