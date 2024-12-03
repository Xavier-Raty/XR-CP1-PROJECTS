# Xavier Raty Rock, Paper, Scissors

import random

def choose_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors against your computer")
        print("Type 'rock', 'paper', or 'scissors' to play.")
        print("Or type 'quit' to exit the game.")
        
        user_choice = input("Your choice: ")
        
        if user_choice == 'quit':
            exit()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("That is not an option. Type 'rock', 'paper', or 'scissors' to play.")
        
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        result = choose_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        print(f"Score: You: {user_score}, Computer: {computer_score}")
    
    print("\nThanks for playing!")
    print(f"Final Score: You: {user_score}, Computer: {computer_score}")