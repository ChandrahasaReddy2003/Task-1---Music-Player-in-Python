import tkinter as tk
import pygame
import os

pygame.init()
music_directory = "D:\music/"
music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")]

pygame.mixer.init()
current_track = 0
pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
pygame.mixer.music.play()

# Function to update the display with the current song name
def update_display(song_name):
    now_playing_label.configure(text="Now Playing: " + song_name)

def play_pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        play_pause_button.configure(text="Play")
    else:
        pygame.mixer.music.unpause()
        play_pause_button.configure(text="Pause")

def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
    pygame.mixer.music.play()
    update_display(music_files[current_track])

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_directory, music_files[current_track]))
    pygame.mixer.music.play()
    update_display(music_files[current_track])

window = tk.Tk()
window.title("Music Player")

now_playing_label = tk.Label(window, text="Now Playing: ")
now_playing_label.pack(pady=10)

play_pause_button = tk.Button(window, text="Pause", command=play_pause)
play_pause_button.pack(pady=10)

next_button = tk.Button(window, text="Next", command=next_track)
next_button.pack(pady=10)

prev_button = tk.Button(window, text="Previous", command=prev_track)
prev_button.pack(pady=10)

update_display(music_files[current_track])

window.mainloop()

pygame.mixer.quit()
pygame.quit()
