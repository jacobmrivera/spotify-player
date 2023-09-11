import tkinter
import customtkinter



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callbck)
        self.button.pack(padx=20, pady=20)

        self.label = customtkinter.CTkLabel(self, text="THIS IS MY LABEL", fg_color="transparent")
        self.label.pack(padx=20, pady=20)
    
    def button_callbck(self):
        print("button clicked")


    



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

    # Run app
    app.mainloop()