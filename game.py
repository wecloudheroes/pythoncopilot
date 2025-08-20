def start_game():
    print("Welcome to the Game!")
    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}! Let's begin...")
    # Initialize game state
    game_state = {
        "player_name": player_name,
        "score": 0,
        "level": 1
    }
    # Start the first level
    start_level(game_state)

def start_level(state):
    print(f"Starting Level {state['level']}...")
    # Simulate gameplay
    for i in range(3):
        answer = input("What is 2 + 2? ")
        if answer == "4":
            print("Correct!")
            state['score'] += 1
        else:
            print("Incorrect!")
    # Level complete
    complete_level(state)

def complete_level(state):
    print(f"Level {state['level']} complete!")
    print(f"Your score: {state['score']}")
    # Check if player wants to continue
    continue_game = input("Do you want to continue to the next level? (yes/no) ")
    if continue_game.lower() == "yes":
        state['level'] += 1
        start_level(state)
    else:
        end_game(state)

def end_game(state):
    print("Thank you for playing!")
    print(f"Your final score: {state['score']}")
    # Save game state to a file
    with open("savefile.txt", "w") as f:
        f.write(str(state))
    print("Game state saved.")
