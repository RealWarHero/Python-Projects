import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            raise ValueError("The length must be a positive integer.")
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    except ValueError as val_err:
        messagebox.showerror("Invalid Input", str(val_err))

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

window = tk.Tk()
window.title("Password Generator")
window.geometry("400x200")

tk.Label(window, text="Enter password length:").pack(pady=10)
entry = tk.Entry(window)
entry.pack(pady=5)

password_var = tk.StringVar()
tk.Entry(window, textvariable=password_var, state='readonly', width=30).pack(pady=10)

tk.Button(window, text="Generate", command=generate_password).pack(pady=5)
tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

window.mainloop()
