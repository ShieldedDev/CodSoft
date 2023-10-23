import random

# Function to get user input
def usr_input():
    user_choice = input("Rock, Paper, or Scissors? ").strip().lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Please choose Rock, Paper, or Scissors: ").strip().lower()
    return user_choice

# Function to generate computer input
def computer_input():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

# Function to determine the winner using an if-else ladder
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "scissors":
            return f"You win! Computer chose {computer_choice}."
        else:
            return f"Computer wins! Computer chose {computer_choice}."
    elif user_choice == "scissors":
        if computer_choice == "paper":
            return f"You win! Computer chose {computer_choice}."
        else:
            return f"Computer wins! Computer chose {computer_choice}."
    else:
        if computer_choice == "rock":
            return f"You win! Computer chose {computer_choice}."
        else:
            return f"Computer wins! Computer chose {computer_choice}."

# Function to play the game
def game():
    user_choice = usr_input()
    computer_choice = computer_input()
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))

# Start the game
game()
