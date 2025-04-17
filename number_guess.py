import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game 🎯")
        self.root.geometry("400x350")
        self.root.configure(bg="#2E3440")

        self.secret_number = random.randint(1, 75)
        self.attempts_left = 7

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Guess the Number!", font=("Arial", 20, "bold"), bg="#2E3440", fg="#88C0D0")
        self.title_label.pack(pady=15)

        self.instruction_label = tk.Label(self.root, text="I'm thinking of a number between 1 and 75.\nYou have 7 tries.", font=("Arial", 12), bg="#2E3440", fg="#D8DEE9")
        self.instruction_label.pack(pady=5)

        self.entry = tk.Entry(self.root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit Guess", font=("Arial", 12, "bold"), bg="#5E81AC", fg="white", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 12), bg="#2E3440", fg="#ECEFF4")
        self.feedback_label.pack(pady=10)

        self.status_label = tk.Label(self.root, text=f"Attempts left: {self.attempts_left}", font=("Arial", 10), bg="#2E3440", fg="#A3BE8C")
        self.status_label.pack(pady=5)

    def check_guess(self):
        guess = self.entry.get()
        if not guess.isdigit():
            self.feedback_label.config(text="🚫 Please enter a valid number.")
            return

        guess = int(guess)
        self.attempts_left -= 1
        self.status_label.config(text=f"Attempts left: {self.attempts_left}")

        if guess == self.secret_number:
            self.feedback_label.config(text=f"🎉 Correct! The number was {self.secret_number}. You win!")
            print(1)  # For arcade score tracking
            self.end_game()
        elif guess < self.secret_number:
            self.feedback_label.config(text="🔻 Too low!")
        else:
            self.feedback_label.config(text="🔺 Too high!")

        if self.attempts_left == 0 and guess != self.secret_number:
            self.feedback_label.config(text=f"😞 Out of tries! The number was {self.secret_number}.")
            print(0)  # For arcade score tracking
            self.end_game()

    def end_game(self):
        self.entry.config(state="disabled")
        self.submit_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingGame(root)
    root.mainloop()
