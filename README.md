# 🎪 Project Funhouse 🎪

A collection of fun, browser-based games built with Python Flask and HTML5 Canvas. Choose your adventure and test your skills across multiple game genres!

## 🎮 Available Games

### 🧺 Emoji Catcher
Catch falling emojis to score points while avoiding dangerous ones! Test your reflexes as the game speeds up.

**How to Play:**
- **Move Left:** ← Arrow key or A
- **Move Right:** → Arrow key or D
- **Catch Good Emojis:**
  - ⭐ Star = +10 points
  - 💎 Diamond = +25 points
  - 💰 Money Bag = +50 points
- **Avoid Bad Emojis:**
  - 💣 Bomb = Lose 1 life
  - ☠️ Skull = Lose 2 lives
- Start with 3 lives and level up as the speed increases!

### 🎯 Target Master
Test your aim and reflexes in this fast-paced target shooting game.

**How to Play:**
- Click on targets as they appear
- Score points for accuracy and speed
- Watch out - targets appear and disappear quickly!
- Beat your high score with precision aiming

### 🧩 Puzzle Quest
Solve sliding tile puzzles by arranging numbered tiles in order.

**How to Play:**
- Click tiles adjacent to the empty space to slide them
- Arrange tiles in numerical order (1-8 or more depending on difficulty)
- Choose from multiple difficulty levels:
  - **Easy:** 3x3 grid (8 tiles)
  - **Medium:** 4x4 grid (15 tiles)
  - **Hard:** 5x5 grid (24 tiles)
- Track your moves and try to solve it in as few moves as possible!

## 🚀 Installation & Running

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/94aharris/project-funhouse.git
   cd project-funhouse
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Play in your browser:**
   - Open your web browser
   - Navigate to: `http://localhost:5000`
   - Choose a game from the menu and have fun!

## 🎨 Features

- **Multiple Games:** Three unique games with different gameplay styles
- **Beautiful UI:** Colorful gradient backgrounds and smooth animations
- **Responsive Design:** Works on desktop and mobile browsers
- **Progressive Difficulty:** Games get harder as you improve
- **Score Tracking:** Real-time score and statistics for each game
- **Pure Web Stack:** No external dependencies - just HTML5, CSS3, and JavaScript

## 🛠️ Technical Details

- **Backend:** Python Flask web framework
- **Frontend:** HTML5 Canvas for game rendering
- **Game Logic:** Vanilla JavaScript
- **Styling:** CSS3 with gradients and animations
- **Architecture:** Clean separation between games with templating

## 📝 Project Structure

```
project-funhouse/
├── app.py                      # Flask application with routes
├── requirements.txt            # Python dependencies
├── templates/
│   ├── index.html             # Main menu/game selector
│   ├── emoji-catcher.html     # Emoji Catcher game
│   ├── target-master.html     # Target Master game
│   └── puzzle-quest.html      # Puzzle Quest game
└── README.md                  # This file
```

## 🎯 Game Routes

- `/` - Main menu (game selector)
- `/game/emoji-catcher` - Emoji Catcher game
- `/game/target-master` - Target Master game
- `/game/puzzle-quest` - Puzzle Quest game

## 🚀 Future Ideas

- Add high score persistence with database
- Implement multiplayer capabilities
- Add more games to the collection
- Create difficulty settings for all games
- Add sound effects and background music
- Implement achievements and unlockables

## 🎉 Credits

Created with GenAI for fun and learning! Feel free to contribute or add your own games to the funhouse.

## 📄 License

Open source - feel free to use, modify, and share!
