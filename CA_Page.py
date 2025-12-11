

import customtkinter

# Set the appearance mode (e.g., "Dark", "Light", "System")
customtkinter.set_appearance_mode("System")
# Set the default color theme (e.g., "blue", "dark-blue", "green")
customtkinter.set_default_color_theme("dark-blue")

# Create the main window
app = customtkinter.CTk()
app.title("My CustomTkinter Window")
app.geometry("400x300")

# Create a button
def button_function():
    print("Button pressed!")

button = customtkinter.CTkButton(master=app, text="Press Me", command=button_function)
button.pack(pady=20)

# Create a label
label = customtkinter.CTkLabel(master=app, text="Welcome to CustomTkinter!")
label.pack()

# Run the application
app.mainloop()