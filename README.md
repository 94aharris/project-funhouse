# 🎮 Emoji Catcher - Project Funhouse 🎮

A fun, browser-based game where you catch falling emojis to score points while avoiding dangerous ones! Built with Python Flask and HTML5 Canvas.

## 🎯 Game Objective

Control a basket to catch good emojis (stars, gems, money) while avoiding bad ones (bombs and skulls). Rack up points, survive as long as possible, and see how high you can score!

## 🕹️ How to Play

- **Move Left:** ← Arrow key or A
- **Move Right:** → Arrow key or D
- **Catch Good Emojis:**
  - ⭐ Star = +10 points
  - 💎 Diamond = +25 points
  - 💰 Money Bag = +50 points
- **Avoid Bad Emojis:**
  - 💣 Bomb = Lose 1 life
  - ☠️ Skull = Lose 2 lives
- You start with 3 lives (❤️❤️❤️)
- The game gets faster as you level up!

## 🚀 Installation & Running

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the game:**
   ```bash
   python app.py
   ```

3. **Play in your browser:**
   - Open your web browser
   - Navigate to: `http://localhost:5000`
   - Click "START GAME" and have fun!

## 🎨 Features

- Colorful gradient backgrounds
- Smooth emoji animations
- Progressive difficulty (speed increases with levels)
- Real-time score tracking
- Lives system with visual hearts
- Level progression
- Responsive controls
- Game over screen with final score

## 🛠️ Technical Details

- **Backend:** Python Flask web framework
- **Frontend:** HTML5 Canvas for rendering
- **Game Logic:** Vanilla JavaScript
- **Styling:** CSS3 with gradients and animations

## 📝 Project Structure

```
project-funhouse/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Game interface and logic
└── README.md          # This file
```

## 🎉 Credits

Created with GenAI for fun and learning!
