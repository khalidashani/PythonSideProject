# Refactoring and improve the code structure

import random

# ensuring the key and value have neccessary emoji
emojis = {'r':'🪨','s':'✂️', 'p':'📄'}
choices = ('r', 'p', 's')

# separate the main code into different function to help in debugging process should encounter any issue
# checking user choice
def get_user_choice():
    while True:
        user = input('Rock, paper, or scissors? (r,p,s): ').lower()
        if user in choices:
            return user
        else:
            print('Invalid choice!')

# display each player choice
def display_choices(user, computer):
    print(f'You chose {emojis[user]}')
    print(f'Computer chose {emojis[computer]}')

# see who is the winner
def determine_winner(user, computer):
    if user == computer:
        print('Tie')
    elif(
        (user == 'r' and computer == 's') or
        (user =='s' and computer == 'p') or
        (user == 'p' and computer =='r')):
        print('You win')
    else:
        print('You lose')

# check if user want to try again or quit
def ask_proceed():
    proceed = input("Continue? (y/n): ").strip().lower()
    if proceed not in ("y", "n"):
        return "invalid"
    return proceed

# function to run all of the function
def play_game():
    while True:
        user = get_user_choice()

        computer = random.choice(choices)

        display_choices(user, computer)

        determine_winner(user, computer)

# after completion of the function, asking user if they want to proceed or quit the program
        
        proceed = ask_proceed()
        if proceed == "invalid":
            print("Invalid choice, try again")
            continue
        elif proceed == "n":
            print("Thanks for playing!")
            break

# run the game
play_game()
