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
main()