import tkinter as tk
import random

# Game choices
choices = ['Rock', 'Paper', 'Scissors']

# Game logic
def determine_winner(user, comp):
    if user == comp:
        return "It's a Tie!"
    elif (user == 'Rock' and comp == 'Scissors') or \
         (user == 'Paper' and comp == 'Rock') or \
         (user == 'Scissors' and comp == 'Paper'):
        return "You Win!"
    else:
        return "Computer Wins!"

# Score tracking
user_score = 0
computer_score = 0

# Function called on user's choice
def play(user_choice):
    global user_score, computer_score
    comp_choice = random.choice(choices)
    result = determine_winner(user_choice, comp_choice)
    
    if "You Win" in result:
        user_score += 1
    elif "Computer Wins" in result:
        computer_score += 1

    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {comp_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Create main window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("400x350")

# Title
title_label = tk.Label(window, text="Choose Rock, Paper or Scissors", font=("Helvetica", 16))
title_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play('Rock'))
paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play('Paper'))
scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play('Scissors'))

rock_button.grid(row=0, column=0, padx=5)
paper_button.grid(row=0, column=1, padx=5)
scissors_button.grid(row=0, column=2, padx=5)

# Result display
result_label = tk.Label(window, text="", font=("Helvetica", 14), fg="blue")
result_label.pack(pady=20)

# Score display
score_label = tk.Label(window, text="Score - You: 0 | Computer: 0", font=("Helvetica", 12))
score_label.pack()

# Quit button
quit_button = tk.Button(window, text="Quit", command=window.quit)
quit_button.pack(pady=10)

# Run the GUI
window.mainloop()
