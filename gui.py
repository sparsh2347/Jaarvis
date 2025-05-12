import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import sys,io
import os

def run_jaarvis():
    link = link_entry.get().strip()
    prompt = prompt_text.get("1.0", tk.END).strip()
    file_name=sol_name.get().strip()

    if not link:
        messagebox.showwarning("Missing Input", "Please enter the assignment link.")
        return

    # Save user input to a temp config file or pass as args/env
    with open("user_input.txt", "w", encoding="utf-8") as f:
        f.write(f"{link}\n")
        f.write(f"{prompt}\n")
        f.write(f"{file_name}\n")

    try:
        subprocess.run(["python", "auto_submit.py"], check=True)
        messagebox.showinfo("Success", "Jaarvis completed the automation!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Something went wrong running Jaarvis.")

# GUI setup
root = tk.Tk()
root.title("Jaarvis Automation")
root.geometry("600x400")

tk.Label(root, text="📎 Assignment Link:").pack(pady=(10, 0))
link_entry = tk.Entry(root, width=70)
link_entry.pack(pady=5)

tk.Label(root, text="✍️ Custom Prompt (optional):").pack(pady=(10, 0))
prompt_text = tk.Text(root, height=5, width=70)
prompt_text.pack(pady=5)

tk.Label(root, text="Solution File Name:").pack(pady=(10, 0))
sol_name= tk.Entry(root,width=70)
sol_name.pack(pady=5)

tk.Button(root, text="🚀 Run Jaarvis", command=run_jaarvis, bg="green", fg="white", width=20).pack(pady=20)


root.mainloop()
