# Aria Febres - Python 3.13
# Date: 10/10/2021
# Description: This program will create a music library for a user to input their music.
# It will also allow the user to search for a song, artist, or album in their library.
# The user will be able to play, pause, stop, skip, shuffle, and repeat songs in their library.
# The user will also be able to create and delete playlists.
# The user will be able to save their music library and playlists to a file.
# The user will be able to load their music library and playlists from a file.
# The user will be able to print their music library and playlists to the console.
# The user will be able to clear their music library and playlists.
# The user will be able to quit the program.
import LibraryClass as Library
import SongClass as Song
import PlaylistManager as Playlist
import saveLoadLibrary as saveLoad
import time

def border():
    print("--------------------------------------------------")

def main():
    #Timing variable to pace print statement for user
    sleep_timing = 1

    # Welcome message
    border()
    print("Welcome to the Music Library!"
          "Here you can create your own music library and playlists.",
          sep="\n")
    time.sleep(sleep_timing)
    print("Let's get started!")
    time.sleep(sleep_timing)
    print("")
    border()
    library = Library()
    playlist_manager = Playlist(library)

    while True:
        border()
        print("Music Library Menu:")
        print("1. Add Song")
        print("2. Create Playlist")
        print("3. Add Song to Playlist")
        print("4. Display Playlists")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter song title: ")
            artist = input("Enter artist: ")
            album = input("Enter album: ")
            year = input("Enter year: ")
            duration = input("Enter duration: ")
            album_art = input("Enter album art: ")
            song = Song(title, artist, album, year, duration, album_art)
            library.add_song(song)
            print("Song added successfully.")
        elif choice == '2':
            playlist_name = input("Enter playlist name: ")
            library.create_playlist(playlist_name)
            print("Playlist created successfully.")
        elif choice == '3':
            playlist_name = input("Enter playlist name: ")
            song_title = input("Enter song title to add: ")
            song = next((s for s in library.songs if s.title == song_title), None)
            if song:
                library.add_song_to_playlist(playlist_name, song)
                print("Song added to playlist successfully.")
            else:
                print("Song not found in library.")
        elif choice == '4':
            playlist_manager.display_playlists()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()