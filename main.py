import customtkinter as ctk

APP_GEOMETRY = "900x700"
APP_TITLE = "Encription App"

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("Dark") 
        self.geometry(APP_GEOMETRY)
        self.title(APP_TITLE)
    