import pygame
import os

pygame.init()

# Set up the display window (optional)
pygame.display.set_mode((800, 600))

# Set up the directory containing your music files
music_directory = "D:\music/"

# Get a list of all the music files in the directory
music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")]

# Initialize the pygame mixer module
pygame.mixer.init()

# Load the first music file
current_track = 0
pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))

# Play the music
pygame.mixer.music.play()

# Main loop
running = True
while running:
    print("Music Player Menu:")
    print("1. Play/Pause")
    print("2. Next Track")
    print("3. Previous Track")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    elif choice == "2":
        current_track = (current_track + 1) % len(music_files)
        pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
        pygame.mixer.music.play()
    elif choice == "3":
        current_track = (current_track - 1) % len(music_files)
        pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
        pygame.mixer.music.play()
    elif choice == "4":
        running = False
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")

# Quit the pygame mixer module
pygame.mixer.quit()

# Quit pygame
pygame.quit()
