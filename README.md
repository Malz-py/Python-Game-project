# 🎮 Python Game Arcade

Welcome to the **Python Game Arcade**, a desktop-based game hub built with `Tkinter`! This project features multiple mini-games in one sleek interface. Track your scores, view your game statistics, and enjoy classic fun — all in one app.

---

## 🕹️ Games Included

| Game Name        | Description |
|------------------|-------------|
| 🧠 Memory Match   | Match pairs of cards using your memory. |
| 🔢 Number Guessing | Guess the number randomly chosen by the computer. |
| ❌⭕ Tic-Tac-Toe   | Classic 2-player or AI battle in a grid-based strategy game. |
| 🏓 Pong            | Paddle vs paddle — keep the ball in play and beat your opponent! |

---

## 🧰 Features

- 🎨 Intuitive Tkinter GUI
- 📊 Score tracking with stats like high score, average score, total plays
- 💾 Persistent data using JSON
- 📁 Modular file structure for each game
- ✅ Works on Windows, macOS, and Linux

---

## 🛠️ Installation

```bash
# 1. Clone this repository
git clone https://github.com/yourusername/python-game-arcade.git
cd python-game-arcade

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt  # For PIL, if used

# 4. Run the arcade
python main.py
