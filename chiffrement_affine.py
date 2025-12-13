import customtkinter as ctk

class ChiffrementAffine(ctk.CTkFrame):
    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self.chiffre = None
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

        output_label = ctk.CTkLabel(self, text="Output:", font=("Arial", 12))
        output_label.pack(pady=(50,5))

        self.cripted_container = ctk.CTkFrame(self)
        self.cripted_container.pack(anchor="center")

        self.cripted_label = ctk.CTkEntry(self.cripted_container, 
                                            width=200, height=30, corner_radius=10, 
                                            fg_color=("lightgray", "white"), text_color="lightgray", 
                                            state="readonly")
        self.cripted_label.configure(state="normal")
        self.cripted_label.delete(0, "end")
        self.cripted_label.insert(0, "Nothing submitted")
        self.cripted_label.configure(state="readonly")
        self.cripted_label.pack(side="left", padx=(0,5))

        copy_button = ctk.CTkButton(self.cripted_container, text="Copy", width=80, height=30,
                                        command=self.copy_message)
        copy_button.pack(side="left")

    def create_widgets(self):
        titre = ctk.CTkLabel(self, text="Encription avec Chiffrement Affine", font=("Impact", 32, "bold"))
        titre.pack(pady=(50,30))
        button = ctk.CTkButton(self, text="Incript Message", 
                               command=self.button_appear_input_feild, width=300, height=75)
        button.pack(pady=(50,50))

    def validate_entry(self):
        char_inconnu = set()
        message = self.entry_field.get().strip()

        if hasattr(self, "message_label"):
            self.message_label.destroy()
            del self.message_label
        if hasattr(self, "after_id"):
            self.after_cancel(self.after_id)

        for char in message: # pour chaque charactere dans le mot de passe
            if char not in self.main.legende.keys():
                char_inconnu.add(char)
        
        if len(char_inconnu) == 1:
            if not hasattr(self, "message_label"):
                self.message_label = ctk.CTkLabel(self, text=f"Le charactère \" {list(char_inconnu)[0]} \" est inconnu dans la légende"
                                            ,font=("Arial", 12), text_color="red")
                self.message_label.pack(pady=30)
                self.after_id = self.after(4000, lambda: self.destroy_message())
        elif len(char_inconnu) != 0:
            if not hasattr(self, "message_label"):
                text = str()

                for char in char_inconnu:
                    if len(text) == 0:
                        text += char
                    if char not in text:
                        text += ", " + char

                self.message_label = ctk.CTkLabel(self, text=f"Les charactères \" {text} \" sont inconnus dans la légende"
                                            ,font=("Arial", 12), text_color="red")
                self.message_label.pack(pady=30)
                self.after_id = self.after(4000, lambda: self.destroy_message())   
        else :
            self.main.message = message
            self.entry_field.delete(0, "end")
            self.focus()
            self.coder_message()
    
    def coder_message(self):
        chiffre = str()
        for lettre in self.main.message:
            nb = ((self.main.legende[lettre] * self.main.alpha) + self.main.beta) % self.main.d
            for key, value in self.main.legende.items():
                if value == nb:
                    chiffre += key
        self.chiffre = chiffre
        self.cripted_label.configure(state="normal", text_color="Black")
        self.cripted_label.delete(0, "end")
        self.cripted_label.insert(0, self.chiffre)
        self.cripted_label.configure(state="readonly")
    
    def copy_message(self):
        self.clipboard_clear()
        self.clipboard_append(self.chiffre)
        self.update()

    def destroy_message(self):
        if hasattr(self, "message_label"):
            self.message_label.destroy()
            del self.message_label
        if hasattr(self, "after_id"):
            self.after_cancel(self.after_id)
