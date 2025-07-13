import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation selected.")
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Input fields
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Operation selection
tk.Label(root, text="Select operation:").pack()
operation_var = tk.StringVar(root)
operation_var.set('+')  # default value

operations_menu = tk.OptionMenu(root, operation_var, '+', '-', '*', '/')
operations_menu.pack()

# Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.pack(pady=10)

# Result display
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run the GUI event loop
root.mainloop()
