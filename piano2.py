import tkinter as tk
import pygame


pygame.init()



def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(0)



def on_key_press(key):
    sound_file = "Hear Piano Note - Mid F.mp3"
    play_sound(sound_file)



root = tk.Tk()
root.title("Simple Piano")


keys = ["C", "D", "E", "F", "G", "A", "B", "C2", "D2", "E2", "F2", "G2", "A2"]

for i, key in enumerate(keys):
    button = tk.Button(root, text=key, width=4, height=10, padx=2, pady=2,
                       font=('Helvetica', 8, 'bold'),
                       relief=tk.RAISED, bd=4, bg="white",
                       command=lambda k=key: on_key_press(k))


    if key[0] != "E" and key[0] != "B":
        button.grid(row=0, column=i * 2, rowspan=2, sticky='nsew', ipadx=5)
    else:
        button.grid(row=0, column=i * 2, rowspan=2, sticky='nsew', ipadx=5)
        button.config(bg="black", height=6)


for i in range(len(keys) * 2):
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(i * 2, weight=1)

root.mainloop()

