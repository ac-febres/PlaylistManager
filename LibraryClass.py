import json
from SongClass import Song
from PlaylistManager import PlaylistManager

# Library.py
class Library:
    def __init__(self):
        self.songs = []
        self.playlists = {}

    def add_song(self, song):
        self.songs.append(song)

    def create_playlist(self, playlist_name):
        if playlist_name not in self.playlists:
            self.playlists[playlist_name] = []
        else:
            print(f"Playlist {playlist_name} already exists.")

    def add_song_to_playlist(self, playlist_name, song):
        if playlist_name in self.playlists:
            self.playlists[playlist_name].append(song)
        else:
            print(f"Playlist {playlist_name} does not exist.")

    def save_library(self, filename):
        with open(filename, 'w') as file:
            json.dump({
                'songs': [song.__dict__ for song in self.songs],
                'playlists': self.playlists
            }, file)

    def load_library(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.songs = [Song(**song) for song in data['songs']]
            self.playlists = data['playlists']