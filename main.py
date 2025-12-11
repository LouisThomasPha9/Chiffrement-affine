import customtkinter as ctk
import json

APP_GEOMETRY = "900x700"
APP_TITLE = "Encription App"

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("Dark") 
        self.geometry(APP_GEOMETRY)
        self.title(APP_TITLE)
        self.legende = json.load(open("characteres.json"))[0]
        self.d = json.load(open("characteres.json"))[1]
        print(self.d)

if __name__ == "__main__":
    app = MainApp() 
    app.mainloop()