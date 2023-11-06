import tkinter as tk
from PIL import ImageTk, Image
import main

APP_WIDTH = main.APP_WIDTH
APP_HEIGHT = main.APP_HEIGHT

class App:
    def __init__(self, root, sp, albumSize):
        self.root = root
        self.root.title("My Tkinter App")
        self.sp = sp

        # Set the size of the application window (width x height)
        root.geometry("{}x{}".format(APP_WIDTH, APP_HEIGHT))

        # Create and configure widgets
        self.label = tk.Label(root, text="Hello, Tkinter!")
        self.button = tk.Button(root, text="Click me", command=self.on_button_click)
        self.albumArt = tk.Label(root)

        default_image = Image.open("album.png")
        self.tk_default_image = ImageTk.PhotoImage(default_image)
        album_pixels = main.get_pixel_num_for_album()
        self.albumArt = tk.Label(root, image=self.tk_default_image, width=album_pixels, height=album_pixels)#, image=ImageTk.PhotoImage(Image.open("album.png"))

        # Pack or grid the widgets
        self.albumArt.pack()
        self.label.pack()
        self.button.pack()
        # self.tk_default_image.pack()

        self.current_song = None
         # Start the mainloop
        self.root.after(0, self.check_song_change)

    def on_button_click(self):
        # Define the behavior when the button is clicked
        print("Button clicked!")

    def load_album_img(self):
        image = tk.PhotoImage(file="album.png")

    def set_new_album_art(self):
        # Load a new image
        new_image = Image.open("album.png")
        new_image_obj = ImageTk.PhotoImage(new_image)

        self.albumArt.config(image=new_image_obj)
        self.albumArt.image = new_image_obj

    def check_song_change(self):
        now_track = self.sp.current_playback()

        if now_track is not None:

            # Get the current track's ID
            now_track_id = now_track['item']['id']
            if now_track_id != self.current_song:
                self.current_song = now_track_id
                print("song change!")
                self.root.after(1000, self.check_song_change)  # Schedule the function to run every second

                return True


            print("same song")
            self.root.after(1000, self.check_song_change)  # Schedule the function to run every second


    def start(self):
        # Start the main loop when you're ready
        self.root.mainloop()
