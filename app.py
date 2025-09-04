from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True
app.config['DEBUG'] = os.getenv('DEBUG', 'False').lower() == 'true'

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
        if 'reset' in request.form:
            session['score'] = {'user': 0, 'computer': 0, 'tie': 0}
            score = session['score']
        else:
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

@app.route('/spinwheel', methods=['GET', 'POST'])
def spinwheel():
    # Initialize session if not exists
    if 'wheel_items' not in session:
        session['wheel_items'] = {}  # Using dict to store item:frequency pairs
    
    if request.method == 'POST':
        if 'add_item' in request.form:
            item = request.form.get('item', '').strip()
            if item:  # Only add non-empty items
                # Get current items dictionary
                current_items = session.get('wheel_items', {})
                if not isinstance(current_items, dict):
                    current_items = {}  # Reset if not a dictionary
                # Increment frequency or add new item
                current_items[item] = current_items.get(item, 0) + 1
                session['wheel_items'] = current_items
                session.modified = True
                print(f"Added/updated item: {item} (frequency: {current_items[item]})")
        
        elif 'clear_items' in request.form:
            session['wheel_items'] = {}
            session.modified = True
            print("Cleared all items")
        
        elif 'spin' in request.form and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            items = session.get('wheel_items', {})
            if not isinstance(items, dict):
                items = {}
            if items:
                # Create weighted list based on frequencies
                weighted_items = []
                for item, freq in items.items():
                    weighted_items.extend([item] * freq)
                selected = random.choice(weighted_items)
                print(f"Selected item: {selected}")
                return jsonify({'selected': selected, 'frequency': items[selected]})
            return jsonify({'error': 'No items to spin'})
        
        elif 'spin' in request.form:
            items = session.get('wheel_items', {})
            if not isinstance(items, dict):
                items = {}
            if items:
                weighted_items = []
                for item, freq in items.items():
                    weighted_items.extend([item] * freq)
                selected = random.choice(weighted_items)
                print(f"Selected item: {selected}")
                return {'selected': selected, 'frequency': items[selected]}
            return {'error': 'No items to spin'}

    # Get items for display
    items = session.get('wheel_items', {})
    if not isinstance(items, dict):
        items = {}
        session['wheel_items'] = items
    print(f"Rendering page with items: {items}")
    return render_template('spinwheel.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
