import json

# Library.py
class Library:
    # Existing methods...

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