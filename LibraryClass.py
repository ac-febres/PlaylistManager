class Library:
    def __init__(self, artists, albums, songs):
        self.library = []
        self.playlists = {}
        self.artists = artists
        self.albums = albums
        self.songs = songs


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