from gtts import gTTS
import tkinter as tk
from tkinter import messagebox
import pygame
import os

def convert_to_audio():
    text = text_entry.get()
    if text:
        try:
            tts = gTTS(text=text, lang='en')
           
            tts.save('output.mp3')
            messagebox.showinfo("Success", "Text converted to audio successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter text.")

def play_audio():
    try:

        pygame.mixer.init()
        pygame.mixer.music.load('output.mp3')
        # Play the audio file
        pygame.mixer.music.play()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while playing audio: {str(e)}")


root = tk.Tk()
root.title("Text to Audio Converter")

text_entry = tk.Entry(root, width=40)
text_entry.pack(pady=20)

# Create a button to trigger text-to-audio conversion
convert_button = tk.Button(root, text="Convert to Audio", command=convert_to_audio)
convert_button.pack()

# Create a button to play the audio
play_button = tk.Button(root, text="Play Audio", command=play_audio)
play_button.pack()

# Run the GUI application
root.mainloop()
