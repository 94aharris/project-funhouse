from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/emoji-catcher')
def emoji_catcher():
    return render_template('emoji-catcher.html')

@app.route('/game/puzzle-quest')
def puzzle_quest():
    return render_template('puzzle-quest.html')

@app.route('/game/target-master')
def target_master():
    return render_template('target-master.html')

@app.route('/game/wordle')
def wordle():
    return render_template('wordle.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
