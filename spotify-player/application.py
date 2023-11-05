import tkinter as tk
from PIL import ImageTk, Image

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("My Tkinter App")

        # Create and configure widgets
        self.label = tk.Label(root, text="Hello, Tkinter!")
        self.button = tk.Button(root, text="Click me", command=self.on_button_click)
        self.albumArt = tk.Label(root)#, image=ImageTk.PhotoImage(Image.open("album.png"))
        default_image = Image.open("album.png")
        self.tk_default_image = ImageTk.PhotoImage(default_image)
        self.albumArt = tk.Label(root, image=self.tk_default_image)#, image=ImageTk.PhotoImage(Image.open("album.png"))

        # Pack or grid the widgets
        self.albumArt.pack()
        self.label.pack()
        self.button.pack()
        # self.tk_default_image.pack()

    def on_button_click(self):
        # Define the behavior when the button is clicked
        print("Button clicked!")

    def load_album_img(self):
        image = tk.PhotoImage(file="album.png")

    def start(self):
        # Start the main loop when you're ready
        self.root.mainloop()
