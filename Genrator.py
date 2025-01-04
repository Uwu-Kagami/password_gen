import string
import random
import pyperclip
import tkinter as tk
import os
import platform
import subprocess
from pynput import keyboard


def generate_password():
    password_length = int(password_length_entry.get())
    include_symbols = include_symbols_var.get()
    
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_characters = letters + digits + (symbols if include_symbols else "")
    
    password = ''.join(random.choices(all_characters, k=password_length))
    pyperclip.copy(password)
    password_display.config(text=f"Password: {password}")
    name_of_saver = str(name_to_save_Password.get())
    current_directory = os.getcwd()
    new_directory = os.path.join(current_directory, name_of_saver)
    os.makedirs(new_directory)
    file_path = os.path.join(new_directory, '_.txt')
    file_content = password
    with open(file_path, 'w') as file:
        file.write(file_content)
        if os.path.exists(new_directory):
            subprocess.run(f'explorer "{new_directory}"')
        else:
            print(f"Le chemin spécifié n'existe pas : {new_directory}")
    
    if platform.system() == "Windows":
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast("Password Generator", "Password Generated", duration=5)

root = tk.Tk()
root.title("Password Generator")
root.geometry("220x260")

tk.Label(root, text="Password Length:").pack(pady=5)
password_length_entry = tk.Entry(root)
password_length_entry.pack(pady=5)

tk.Label(root, text="Name To Save It:").pack(pady=5)
name_to_save_Password = tk.Entry(root)
name_to_save_Password.pack(pady=10)

include_symbols_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Symbols", variable=include_symbols_var).pack(pady=5)

tk.Button(root, text="Generate", command=generate_password).pack(pady=20)
password_display = tk.Label(root, text="")
password_display.pack(pady=5)

root.mainloop()



