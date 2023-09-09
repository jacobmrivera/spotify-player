import tkinter
import customtkinter

def startApp():

    # System Settings
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    # Our app frame
    app = customtkinter.CTk()
    app.geometry("720x480")
    app.title("Spotify Player")

    # Adding UI Elements
    title = customtkinter.CTkLabel(app, text="what song")
    title.pack(padx=10, pady=10)
