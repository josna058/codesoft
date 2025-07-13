import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Weak Length", "Password length should be at least 4 characters.")
            return
        
        # Character set for the password
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display password
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length.")

# GUI window setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x200")
root.resizable(False, False)

# Label and input for password length
tk.Label(root, text="Enter Password Length:", font=('Arial', 12)).pack(pady=10)
length_entry = tk.Entry(root, font=('Arial', 12), justify='center')
length_entry.pack()

# Generate button
generate_btn = tk.Button(root, text="Generate Password", font=('Arial', 12), command=generate_password)
generate_btn.pack(pady=15)

# Entry to display the generated password
password_entry = tk.Entry(root, font=('Arial', 12), justify='center', width=30)
password_entry.pack()

# Run the GUI application
root.mainloop()
