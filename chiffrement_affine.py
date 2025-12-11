import customtkinter as ctk

class ChiffrementAffine(ctk.CTkFrame):
    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def button_appear_input_feild(self):
        if hasattr(self, "entry_container"):
            return
        
        self.entry_container = ctk.CTkFrame(self)
        self.entry_container.pack(pady=10, anchor="center")

        self.entry_field = ctk.CTkEntry(self.entry_container, placeholder_text="Enter your message", 
                                   width=200, height=30, corner_radius=10, 
                                   fg_color=("lightgray", "white"), text_color="Black", 
                                   placeholder_text_color="lightgray")
        self.entry_field.pack(side="left", padx=(0,5)) 

        # ça c juste pour lier la fonction validate entry avec la touche enter
        self.entry_field.bind("<Return>", lambda event: self.validate_entry())
        
        entry_button = ctk.CTkButton(self.entry_container, text="Valider", width=80, height=30,
                                        command=self.validate_entry)
        entry_button.pack(side="left")

    def create_widgets(self):
        titre = ctk.CTkLabel(self, text="Encription avec Chiffrement Affine", font=("Impact", 32, "bold"))
        titre.pack(pady=(50,30))
        button = ctk.CTkButton(self, text="Incript Message", 
                               command=self.button_appear_input_feild, width=300, height=75)
        button.pack(pady=(50,50))

    def validate_entry(self):
        MDP = self.entry_field.get().strip()
        for char in MDP: # pour chaque charactere dans le mot de passe
            if char not in self.main.legende.keys():
                print("not in legende")

        print(MDP)
