# PlaylistManager.py
class PlaylistManager:
    def __init__(self, library):
        self.library = library

    def display_playlists(self):
        for playlist_name, songs in self.library.playlists.items():
            print(f"Playlist: {playlist_name}")
            for song in songs:
                print(f"  - {song}")