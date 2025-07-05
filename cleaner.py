import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox
import tkinter as tk

# Function to create a subfolder
def create_subfolder(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path

# Function to clean the selected folder
def clean_folder(folder_path, log_box):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                subfolder_name = f"{file_extension.upper()} files"
                subfolder_path = create_subfolder(folder_path, subfolder_name)
                file_path = os.path.join(folder_path, filename)
                new_location = os.path.join(subfolder_path, filename)
                if not os.path.exists(new_location):
                    shutil.move(file_path, subfolder_path)
                    log_box.insert(tk.END, f"Moved {filename} to {subfolder_name}\n")
                else:
                    log_box.insert(tk.END, f"Skipped {filename} as it already exists in {subfolder_name}\n")
    log_box.insert(tk.END, "Cleaning complete!\n")

# Function to browse for a folder
def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path_entry.delete(0, tk.END)
        folder_path_entry.insert(0, folder_selected)

# Function to start cleaning process
def start_cleaning():
    folder_path = folder_path_entry.get()
    if os.path.isdir(folder_path):
        log_box.delete(1.0, tk.END)  # Clear previous logs
        clean_folder(folder_path, log_box)
    else:
        messagebox.showerror("Error", "Invalid folder path!")

# Create the main window with customtkinter
ctk.set_appearance_mode("dark")  # "light" or "dark" mode
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

window = ctk.CTk()
window.title("Desktop Cleaner")
window.geometry("600x500")

# Folder selection widgets
folder_label = ctk.CTkLabel(window, text="Enter the path of the folder you want to clean:", font=ctk.CTkFont(size=16))
folder_label.pack(pady=10)

folder_path_entry = ctk.CTkEntry(window, width=400)
folder_path_entry.pack(pady=5)

browse_button = ctk.CTkButton(window, text="Browse", command=browse_folder)
browse_button.pack(pady=5)

# Clean button
clean_button = ctk.CTkButton(window, text="Start Cleaning", command=start_cleaning, fg_color="green", hover_color="darkgreen", text_color="white")
clean_button.pack(pady=10)

# Log display (Scrolled Text Box with custom colors)
log_box = ctk.CTkTextbox(window, width=500, height=200)
log_box.pack(pady=10)

# Run the application
window.mainloop()
