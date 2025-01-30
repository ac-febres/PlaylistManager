# Song.py
class Song:
    def __init__(self, title, artist, album, year, duration, album_art):
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        self.duration = duration
        self.album_art = album_art

    def __str__(self):
        return f"{self.title} by {self.artist}"