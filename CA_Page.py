import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("My CustomTkinter Window")
app.geometry("500x500")

def button_appear_input_feild():
    entry_field = ctk.CTkEntry(master=app, placeholder_text="Enter your message", width=200, height=30, corner_radius=10, fg_color=("lightgray", "white"), text_color="Black", placeholder_text_color="lightgray")
    entry_field.pack(pady=10,padx = 10, anchor="center")


button = ctk.CTkButton(master=app, text="Incript Message", command=button_appear_input_feild, width=300, height=75)
button.pack(pady=100)



app.mainloop()