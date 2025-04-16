import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root, difficulty="Easy"):
        self.root = root
        self.root.title("Memory Match")

        # Define difficulty levels
        self.card_sets = {
            "Easy": ["🍎", "🍎", "🍌", "🍌", "🍓", "🍓", "🍇", "🍇"],
            "Medium": ["🍎", "🍎", "🍌", "🍌", "🍓", "🍓", "🍇", "🍇", "🍉", "🍉", "🥝", "🥝"],
            "Hard": ["🍎", "🍎", "🍌", "🍌", "🍓", "🍓", "🍇", "🍇", "🍉", "🍉", "🥝", "🥝", "🍒", "🍒", "🍍", "🍍"]
        }
        
        self.cards = self.card_sets[difficulty]
        random.shuffle(self.cards)
        
        self.buttons = []
        self.flipped = []
        self.score = 0

        self.create_board()

    def create_board(self):
        """Creates the grid of buttons."""
        for i in range(len(self.cards)):
            btn = tk.Button(self.root, text="", width=6, height=3, font=("Arial", 20),
                            command=lambda i=i: self.flip_card(i))
            btn.grid(row=i // 4, column=i % 4)
            self.buttons.append(btn)

        self.label = tk.Label(self.root, text="Find all pairs!", font=("Arial", 16))
        self.label.grid(row=4, columnspan=4)

    def flip_card(self, index):
        """Handles card flipping logic."""
        if len(self.flipped) < 2:
            self.buttons[index].config(text=self.cards[index], state="disabled")
            self.flipped.append(index)

        if len(self.flipped) == 2:
            self.root.after(1000, self.check_match)

    def check_match(self):
        """Checks if the flipped cards match."""
        idx1, idx2 = self.flipped
        if self.cards[idx1] == self.cards[idx2]:
            self.score += 1
        else:
            self.buttons[idx1].config(text="", state="normal")
            self.buttons[idx2].config(text="", state="normal")

        self.flipped.clear()
        self.check_game_end()

    def check_game_end(self):
        """Ends game when all matches are found."""
        if self.score == len(self.cards) // 2:
            for btn in self.buttons:
                btn.config(state="disabled")
            self.label.config(text="Congratulations! You Won!")

# Start game
if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root, difficulty="Medium")  # Change difficulty: Easy, Medium, Hard
    root.mainloop()
