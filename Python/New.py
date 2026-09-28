import random

def play_game():
    # 1. Define choices
    choices = ['s', 'p', 'r']
    
    print("--- Stone, Paper, Scissors Game ---")
    print("Rules: 's' for Stone, 'p' for Paper, 'r' for Scissors")
    
    # 2. Get user input
    user_choice = input("Enter your choice (s/p/r): ").lower()
    
    if user_choice not in choices:
        print("Invalid choice! Please restart and pick 's', 'p', or 'r'.")
        return

    # 3. Computer's choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # 4. Determine result
    if user_choice == computer_choice:
        print("It's a Tie!")
    
    elif (user_choice == 's' and computer_choice == 'r') or \
         (user_choice == 'p' and computer_choice == 's') or \
         (user_choice == 'r' and computer_choice == 'p'):
        print("You Win!")
        
    else:
        print("You Lose!")

# Run the game
play_game()