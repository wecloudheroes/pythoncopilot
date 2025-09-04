import random

def get_user_choice():
    choices = ['stone', 'paper', 'scissor']
    user_input = input("Enter your choice (stone/paper/scissor): ").lower()
    while user_input not in choices:
        print("Invalid choice. Try again.")
        user_input = input("Enter your choice (stone/paper/scissor): ").lower()
    return user_input

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissor'])

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'stone' and computer == 'scissor') or \
         (user == 'paper' and computer == 'stone') or \
         (user == 'scissor' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Stone, Paper, Scissor!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(decide_winner(user_choice, computer_choice))
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

            # You can add a function to display the game rules
            def show_rules():
                print("Game Rules:")
                print("- Stone beats Scissor")
                print("- Scissor beats Paper")
                print("- Paper beats Stone")
                print("- If both choose the same, it's a tie!")

            # Optionally, call show_rules() before starting the game
            show_rules()
if __name__ == "__main__":
    play_game()