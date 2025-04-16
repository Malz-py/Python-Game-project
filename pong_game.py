#Malieka Forbes
#Pong Game 

import tkinter as tk

class PongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pong Game")

        # Game settings
        self.width = 800
        self.height = 600
        self.ball_speed = 5
        self.paddle_speed = 30
        self.winning_score = 10  # First to reach 10 wins

        # Initialize score
        self.score = 0
        self.game_over = False

        # Create canvas
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        # Create score label
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Arial", 16), fg="white", bg="black")
        self.score_label.place(x=self.width//2 - 50, y=10)

        # Paddle and ball sizes
        self.paddle_width = 20
        self.paddle_height = 100
        self.ball_size = 20

        # Left paddle
        self.left_paddle = self.canvas.create_rectangle(
            50,
            (self.height // 2) - 50,
            50 + self.paddle_width,
            (self.height // 2) + 50,
            fill="white"
        )

        # Right paddle
        self.right_paddle = self.canvas.create_rectangle(
            self.width - 50 - self.paddle_width,
            (self.height // 2) - 50,
            self.width - 50,
            (self.height // 2) + 50,
            fill="white"
        )

        # Ball
        self.ball = self.canvas.create_oval(
            self.width // 2 - self.ball_size // 2,
            self.height // 2 - self.ball_size // 2,
            self.width // 2 + self.ball_size // 2,
            self.height // 2 + self.ball_size // 2,
            fill="white"
        )

        # Ball direction
        self.ball_dx = self.ball_speed
        self.ball_dy = self.ball_speed

        # Bind movement keys
        self.canvas.bind("<KeyPress-w>", self.move_left_paddle_up)
        self.canvas.bind("<KeyPress-s>", self.move_left_paddle_down)
        self.canvas.bind("<KeyPress-Up>", self.move_right_paddle_up)
        self.canvas.bind("<KeyPress-Down>", self.move_right_paddle_down)
        self.canvas.focus_set()

        # Start the game loop
        self.update_game()

    def move_left_paddle_up(self, event):
        """Move left paddle up"""
        if self.canvas.coords(self.left_paddle)[1] > 0:
            self.canvas.move(self.left_paddle, 0, -self.paddle_speed)

    def move_left_paddle_down(self, event):
        """Move left paddle down"""
        if self.canvas.coords(self.left_paddle)[3] < self.height:
            self.canvas.move(self.left_paddle, 0, self.paddle_speed)

    def move_right_paddle_up(self, event):
        """Move right paddle up"""
        if self.canvas.coords(self.right_paddle)[1] > 0:
            self.canvas.move(self.right_paddle, 0, -self.paddle_speed)

    def move_right_paddle_down(self, event):
        """Move right paddle down"""
        if self.canvas.coords(self.right_paddle)[3] < self.height:
            self.canvas.move(self.right_paddle, 0, self.paddle_speed)

    def update_game(self):
        """Main game loop"""
        if self.game_over:
            return  # Stop game loop

        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_coords = self.canvas.coords(self.ball)

        # Bounce on top/bottom walls
        if ball_coords[1] <= 0 or ball_coords[3] >= self.height:
            self.ball_dy = -self.ball_dy

        # Paddle collisions
        if self.check_collision_with_paddle(ball_coords, self.left_paddle):
            self.ball_dx = abs(self.ball_dx)
            self.update_score()
        elif self.check_collision_with_paddle(ball_coords, self.right_paddle):
            self.ball_dx = -abs(self.ball_dx)
            self.update_score()

        # Ball out of bounds
        if ball_coords[0] <= 0 or ball_coords[2] >= self.width:
            self.reset_ball()

        # Loop again after 10ms
        self.root.after(10, self.update_game)

    def check_collision_with_paddle(self, ball_coords, paddle):
        """Collision detection with paddle"""
        paddle_coords = self.canvas.coords(paddle)
        if ball_coords[2] >= paddle_coords[0] and ball_coords[0] <= paddle_coords[2]:
            if ball_coords[3] >= paddle_coords[1] and ball_coords[1] <= paddle_coords[3]:
                return True
        return False

    def update_score(self):
        """Add score and update label"""
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")

        if self.score >= self.winning_score:
            self.end_game()

    def reset_ball(self):
        """Reset ball to center and reverse direction"""
        self.canvas.coords(
            self.ball,
            self.width // 2 - self.ball_size // 2,
            self.height // 2 - self.ball_size // 2,
            self.width // 2 + self.ball_size // 2,
            self.height // 2 + self.ball_size // 2
        )
        self.ball_dx = -self.ball_dx
        self.ball_dy = self.ball_speed

    def end_game(self):
        """Show winner and stop game"""
        self.game_over = True
        self.canvas.create_text(
            self.width // 2, self.height // 2,
            text="🏆 You Win! 🏆",
            fill="yellow", font=("Arial", 40)
        )

if __name__ == "__main__":
    root = tk.Tk()
    pong_game = PongGame(root)
    root.mainloop()

