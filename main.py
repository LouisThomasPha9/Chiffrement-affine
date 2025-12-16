import customtkinter as ctk
import json
from chiffrement_affine import ChiffrementAffine

APP_GEOMETRY = "700x700"
APP_TITLE = "Encription App"

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("Dark") 
        ctk.set_default_color_theme("dark-blue")
        self.geometry(APP_GEOMETRY)
        self.title(APP_TITLE)
        self.legende = json.load(open("characteres.json"))[0]
        self.d = json.load(open("characteres.json"))[1]
        self.alpha = 2
        self.beta = 0
        self.message = None
        self.liste_alpha = None
        self.CA_Window = ChiffrementAffine(self)

if __name__ == "__main__":
    app = MainApp() 
    app.mainloop()