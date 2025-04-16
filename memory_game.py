import tkinter as tk
import random
import sys

class MemoryGame:
    def __init__(self, root, difficulty="Easy"):
        self.root = root
        self.root.title("Memory Match 🍒")
        self.root.configure(bg="#2E3440")

        # Define difficulty levels and emojis
        self.card_sets = {
            "Easy": ["🍎", "🍎", "🍌", "🍌", "🍓", "🍓", "🍇", "🍇"],
            "Medium": ["🍎", "🍎", "🍌", "🍌", "🍓", "🍓", "🍇", "🍇", "🍉", "🍉", "🥝", "🥝"],
            "Hard": ["🍎", "🍎", "🍌", "🍌", "🍓", "🍓", "🍇", "🍇", "🍉", "🍉", "🥝", "🥝", "🍒", "🍒", "🍍", "🍍"]
        }

        self.cards = self.card_sets[difficulty]
        random.shuffle(self.cards)

        self.buttons = []
        self.flipped = []
        self.matches_found = 0
        self.total_pairs = len(self.cards) // 2

        self.create_board()

    def create_board(self):
        """Create the grid of cards (buttons)."""
        rows = len(self.cards) // 4
        for i in range(len(self.cards)):
            btn = tk.Button(
                self.root,
                text="",
                width=6,
                height=3,
                font=("Arial", 24, "bold"),
                bg="#4C566A",
                fg="#ECEFF4",
                activebackground="#5E81AC",
                command=lambda i=i: self.flip_card(i)
            )
            btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)
            self.buttons.append(btn)

        self.status_label = tk.Label(
            self.root,
            text="Find all the pairs!",
            font=("Arial", 16, "bold"),
            bg="#2E3440",
            fg="#A3BE8C",
            pady=10
        )
        self.status_label.grid(row=rows + 1, columnspan=4)

    def flip_card(self, index):
        """Flip a card and handle logic."""
        if self.buttons[index]["text"] == "" and len(self.flipped) < 2:
            self.buttons[index].config(text=self.cards[index], state="disabled")
            self.flipped.append(index)

        if len(self.flipped) == 2:
            self.root.after(800, self.check_match)

    def check_match(self):
        """Check if two flipped cards match."""
        idx1, idx2 = self.flipped
        if self.cards[idx1] == self.cards[idx2]:
            self.matches_found += 1
        else:
            # Flip back over
            self.buttons[idx1].config(text="", state="normal")
            self.buttons[idx2].config(text="", state="normal")

        self.flipped.clear()
        self.check_game_end()

    def check_game_end(self):
        """Check if the game has ended and output score."""
        if self.matches_found == self.total_pairs:
            for btn in self.buttons:
                btn.config(state="disabled")

            self.status_label.config(text="🎉 You matched all the pairs! 🎉")

            # Output score to console for arcade tracking
            print(self.matches_found)
            self.root.after(1500, self.root.quit)  # Close after a short delay

# Start game
if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root, difficulty="Medium")  # Change difficulty here if needed
    root.mainloop()
