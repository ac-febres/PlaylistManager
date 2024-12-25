class Song:
    def __init__(self, title, artist, album, year, duration, album_art):
        self.title = title
        self.artist = artist
        self.album = album
        self.year = year
        self.duration = duration
        self.album_art = album_art

    def __str__(self):
        return self.title + " by " + self.artist

class Player(Song):
    def __init__(self, songs):
        self.songs = []

    def play(self):
        print("Playing: " + self.title)

    def pause(self):
        print("Paused: " + self.title)

    def stop(self):
        print("Stopped: " + self.title)

    def next(self):
        print("Playing next song")

    def previous(self):
        print("Playing previous song")

    def shuffle(self):
        print("Shuffling songs")

    def repeat(self):
        print("Repeating song")

class PlaylistManager:
    pass
