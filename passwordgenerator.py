import tkinter as tk
from tkinter import messagebox
import string
import random

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

        self.bg_color = "#ffffff"
        self.text_color = "#333333"
        self.entry_bg_color = "#f0f0f0"
        self.btn_color = "#4CAF50"
        self.btn_text_color = "#ffffff"
        self.password_fg_color = "#d9534f"

        self.root.config(bg=self.bg_color)

        self.title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18, "bold"), 
                                    bg=self.bg_color, fg=self.text_color)
        self.title_label.pack(pady=20)

        self.length_label = tk.Label(root, text="Enter password length:", font=("Helvetica", 12),
                                     bg=self.bg_color, fg=self.text_color)
        self.length_label.pack(pady=5)

        self.length_entry = tk.Entry(root, font=("Helvetica", 12), width=5, bg=self.entry_bg_color, fg=self.text_color)
        self.length_entry.pack(pady=5)

        self.strength_title_label = tk.Label(root, text="Password Strength:", font=("Helvetica", 12, "bold"),
                                             bg=self.bg_color, fg=self.text_color)
        self.strength_title_label.pack(pady=10)

        self.strength_var = tk.StringVar(value="easy")

        self.easy_radio = tk.Radiobutton(root, text="Easy", variable=self.strength_var, value="easy",
                                         font=("Helvetica", 12), bg=self.bg_color, fg=self.text_color)
        self.easy_radio.pack(pady=5)

        self.moderate_radio = tk.Radiobutton(root, text="Moderate", variable=self.strength_var, value="moderate",
                                             font=("Helvetica", 12), bg=self.bg_color, fg=self.text_color)
        self.moderate_radio.pack(pady=5)

        self.hard_radio = tk.Radiobutton(root, text="Hard", variable=self.strength_var, value="hard",
                                         font=("Helvetica", 12), bg=self.bg_color, fg=self.text_color)
        self.hard_radio.pack(pady=5)

        self.generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12, "bold"),
                                         bg=self.btn_color, fg=self.btn_text_color, command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.clear_button = tk.Button(root, text="Clear", font=("Helvetica", 12, "bold"), bg=self.btn_color,
                                      fg=self.btn_text_color, command=self.clear_password)
        self.clear_button.pack(pady=10)

        self.password_label = tk.Label(root, text="", font=("Helvetica", 12, "bold"), bg=self.bg_color,
                                       fg=self.password_fg_color)
        self.password_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Password length must be at least 1!")

            strength = self.strength_var.get()

            if strength == "easy":
                characters = string.ascii_lowercase
            elif strength == "moderate":
                characters = string.ascii_letters + string.digits
            else:
                characters = string.ascii_letters + string.digits + string.punctuation

            password = ''.join(random.choice(characters) for _ in range(length))

            self.password_label.config(text=password)
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def clear_password(self):
        self.password_label.config(text="")
        self.length_entry.delete(0, tk.END)
        self.strength_var.set("easy")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
