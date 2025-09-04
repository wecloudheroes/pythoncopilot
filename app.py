from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

choices = ['stone', 'paper', 'scissor']

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'stone' and computer == 'scissor') or \
         (user == 'paper' and computer == 'stone') or \
         (user == 'scissor' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

from flask import session

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'score' not in session:
        session['score'] = {'user': 0, 'computer': 0, 'tie': 0}
    result = None
    user_choice = None
    computer_choice = None
    score = session['score']
    if request.method == 'POST':
        user_choice = request.form.get('choice')
        computer_choice = random.choice(choices)
        result = decide_winner(user_choice, computer_choice)
        if result == "You win!":
            score['user'] += 1
        elif result == "Computer wins!":
            score['computer'] += 1
        else:
            score['tie'] += 1
        session['score'] = score
    return render_template('index.html', choices=choices, result=result, user_choice=user_choice, computer_choice=computer_choice, score=score)

if __name__ == '__main__':
    app.run(debug=True)
