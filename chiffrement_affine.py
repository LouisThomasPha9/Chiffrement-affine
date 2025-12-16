import customtkinter as ctk

class ChiffrementAffine(ctk.CTkFrame):
    def __init__(self, main):
        super().__init__(main)
        self.main = main
        self.chiffre = None
        self.decripted = None
        self.alpha_decript = None
        self.beta_decript = None
        self.message_decript = None
        self.pack(fill="both", expand=True)
        self.valeurs_possibles_alpha()
        self.create_widgets()

    def button_appear_input_feild_incript(self):
        if hasattr(self, "entry_container"):
            return
        
        self.entry_container = ctk.CTkFrame(self.cripting_container)
        self.entry_container.pack(pady=10, anchor="center")

        self.entry_field = ctk.CTkEntry(self.entry_container, placeholder_text="Enter your message", 
                                   width=210, height=30, corner_radius=10, 
                                   fg_color=("lightgray", "white"), text_color="Black", 
                                   placeholder_text_color="lightgray")
        self.entry_field.pack(side="left", padx=(0,10)) 

        # ça c juste pour lier la fonction validate entry avec la touche enter
        self.entry_field.bind("<Return>", lambda event: self.validate_entry())
        
        entry_button = ctk.CTkButton(self.entry_container, text="Valider", width=80, height=30,
                                        command=self.validate_entry)
        entry_button.pack(side="left")

        output_label = ctk.CTkLabel(self.cripting_container, text="Output:", font=("Arial", 12))
        output_label.pack(pady=(50,5))

        self.cripted_container = ctk.CTkFrame(self.cripting_container)
        self.cripted_container.pack(anchor="center")

        self.cripted_label = ctk.CTkEntry(self.cripted_container, 
                                            width=210, height=30, corner_radius=10, 
                                            fg_color=("lightgray", "white"), text_color="lightgray", 
                                            state="readonly")
        self.cripted_label.configure(state="normal")
        self.cripted_label.delete(0, "end")
        self.cripted_label.insert(0, "Nothing submitted")
        self.cripted_label.configure(state="readonly")
        self.cripted_label.pack(side="left", padx=(0,10))

        copy_button = ctk.CTkButton(self.cripted_container, text="Copy", width=80, height=30,
                                        command=self.copy_message)
        copy_button.pack(side="left")
    
    def button_appear_input_feild_decript(self):
        if hasattr(self, "entry_container_right"):
            return
        
        self.entry_container_right = ctk.CTkFrame(self.decripting_container)
        self.entry_container_right.pack(pady=10, anchor="center")

        self.entry_field_decription = ctk.CTkEntry(self.entry_container_right, placeholder_text="Enter encripted message", 
                                   width=210, height=30, corner_radius=10, 
                                   fg_color=("lightgray", "white"), text_color="Black", 
                                   placeholder_text_color="lightgray")
        self.entry_field_decription.pack(side="left", padx=(0,10)) 

        self.entry_field_decription.bind("<Return>", lambda event: self.validate_entry_decription()) 

        entry_button_decription = ctk.CTkButton(self.entry_container_right, text="Valider", width=80, height=30,
                                        command=self.validate_entry_decription)
        entry_button_decription.pack(side="left")

        key_label = ctk.CTkLabel(self.decripting_container, text="Keys:", font=("Arial", 12), width=300, anchor="w")
        key_label.pack(pady=(5,5))

        self.key_container = ctk.CTkFrame(self.decripting_container)
        self.key_container.pack()

        alpha_container = ctk.CTkFrame(self.key_container, fg_color="transparent")
        alpha_container.pack(side="left")

        beta_container = ctk.CTkFrame(self.key_container, fg_color="transparent")
        beta_container.pack(side="right", padx=(25,0))

        alpha_label = ctk.CTkLabel(alpha_container, text="Alpha:", font=("Arial", 12), width=65, anchor="w")
        alpha_label.pack(side="left", padx=(0,5))

        l = [str(nb) for nb in self.main.liste_alpha]
        l.insert(0, "Key")
        self.dropdown = ctk.CTkOptionMenu(alpha_container, values=l, width=75, command=self.select_alpha)
        self.dropdown.pack(side="right")

        beta_label = ctk.CTkLabel(beta_container, text="Beta:", font=("Arial", 12), width=65)
        beta_label.pack(side="left")

        self.beta_entry = ctk.CTkEntry(beta_container, width=65, height=30, corner_radius=10, 
                                            placeholder_text="Key",
                                            fg_color=("lightgray", "white"), text_color="Black")
        self.beta_entry.pack(side="right")

        self.beta_entry.bind("<Return>", lambda event: self.validate_entry_beta()) 

        output_label = ctk.CTkLabel(self.decripting_container, text="Output:", font=("Arial", 12))
        output_label.pack(pady=(25,5))

        self.decripted_container = ctk.CTkFrame(self.decripting_container)
        self.decripted_container.pack(anchor="center")

        self.decripted_label = ctk.CTkEntry(self.decripted_container, 
                                            width=210, height=30, corner_radius=10, 
                                            fg_color=("lightgray", "white"), text_color="lightgray", 
                                            state="readonly")
        self.decripted_label.configure(state="normal")
        self.decripted_label.delete(0, "end")
        self.decripted_label.insert(0, "Nothing submitted")
        self.decripted_label.configure(state="readonly")
        self.decripted_label.pack(side="left", padx=(0,10))

        copy_button = ctk.CTkButton(self.decripted_container, text="Copy", width=80, height=30,
                                        command=self.copy_message_decripted)
        copy_button.pack(side="left")

    def create_widgets(self):
        titre = ctk.CTkLabel(self, text="Encription avec Chiffrement Affine", font=("Impact", 32, "bold"))
        titre.pack(pady=(50,30))

        self.main_container = ctk.CTkFrame(self,  fg_color="transparent")
        self.main_container.pack(anchor="center")

        self.cripting_container = ctk.CTkFrame(self.main_container,  fg_color="transparent")
        self.cripting_container.pack(ancho="n", side="left", padx=30)

        self.decripting_container = ctk.CTkFrame(self.main_container,  fg_color="transparent")
        self.decripting_container.pack(anchor="n", side="right", padx=30)

        button = ctk.CTkButton(self.cripting_container, text="Incript Message", 
                               command=self.button_appear_input_feild_incript, width=300, height=75)
        button.pack(pady=(50,50))

        button = ctk.CTkButton(self.decripting_container, text="Decript Message", 
                               command=self.button_appear_input_feild_decript, width=300, height=75)
        button.pack(pady=(50,50))

    @staticmethod
    def pgcd(a,b):
        x = a
        y = b
        r = x%y
        while r != 0:
            x = y
            y = r
            r = x%y
        return y
    
    @staticmethod
    def inverse_modulaire(a, d):
        for i in range(d):
            if (a * i) % d == 1:
                return i
    
    def valeurs_possibles_alpha(self):
        l = list()
        for i in range(self.main.d):
            if self.pgcd(i,self.main.d) == 1:
                l.append(i)
        self.main.liste_alpha = l

    def select_alpha(self, value):
        if value == "Key":
            return
        else:
            self.alpha_decript = value
            if self.beta_decript is not None and self.message_decript is not None:
                self.decoder_message()

    def validate_entry_decription(self):
        char_inconnu = set()
        message = self.entry_field_decription.get().strip()

        if hasattr(self, "message_label"):
            self.message_label.destroy()
            del self.message_label
        if hasattr(self, "after_id"):
            self.after_cancel(self.after_id)

        for char in message: 
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
            self.focus()
            self.message_decript = message
            if self.alpha_decript is not None and self.beta_decript is not None:
                self.decoder_message()

    def decoder_message(self):
        m = str()
        for lettre in self.message_decript:
            for key, value in self.main.legende.items():
                if value == (self.inverse_modulaire(int(self.alpha_decript), self.main.d) * (self.main.legende[lettre] - self.beta_decript)) % self.main.d:
                    m += key
        self.decripted = m
        self.decripted_label.configure(state="normal", text_color="Black")
        self.decripted_label.delete(0, "end")
        self.decripted_label.insert(0, self.decripted)
        self.decripted_label.configure(state="readonly")
    
    def validate_entry_beta(self):
        b = int(self.beta_entry.get().strip())

        if hasattr(self, "message_label"):
            self.message_label.destroy()
            del self.message_label
        if hasattr(self, "after_id"):
            self.after_cancel(self.after_id)

        if b >= self.main.d:
            if not hasattr(self, "message_label"):
                self.message_label = ctk.CTkLabel(self, text=f"Ta clé beta {b} est plus grand que d {self.main.d}"
                                            ,font=("Arial", 12), text_color="red")
                self.message_label.pack(pady=30)
                self.after_id = self.after(4000, lambda: self.destroy_message())
        else:
            self.beta_decript = b
            self.focus()
            if self.alpha_decript is not None and self.message_decript is not None:
                self.decoder_message()

    def validate_entry(self):
        char_inconnu = set()
        message = self.entry_field.get().strip()

        if hasattr(self, "message_label"):
            self.message_label.destroy()
            del self.message_label
        if hasattr(self, "after_id"):
            self.after_cancel(self.after_id)

        for char in message: 
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

    def copy_message_decripted(self):
        self.clipboard_clear()
        self.clipboard_append(self.decripted)
        self.update()

    def destroy_message(self):
        if hasattr(self, "message_label"):
            self.message_label.destroy()
            del self.message_label
        if hasattr(self, "after_id"):
            self.after_cancel(self.after_id)