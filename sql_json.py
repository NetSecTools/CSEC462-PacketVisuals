import json
from sqlobject import *



import sqlite3



def Main():
    # This is an iterable, not a list
    all_songs = Song.select().orderBy(Song.q.name)

    songs_as_dict = []

    for song in all_songs:
        song_as_dict = {
            'name' : song.name,
            'artist' : song.artist,
            'album' : song.album}
        songs_as_dict.append(song_as_dict)

    print simplejson.dumps(songs_as_dict)
