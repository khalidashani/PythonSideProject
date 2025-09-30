# Generate between r, p, s
# User enter between r, p, s
# If user win
#   Say congrants
#   Ask if want to continue
#       If user say y
#           Rerun function
#       If user say n
#           Break the function
# If user lose
#   Say you lose
#   Ask if want to continue
#       If user say y
#           Rerun function
#       If user say n
#           Break the function

import random

emojis = {'r':'🪨','s':'✂️', 'p':'📄'}
choices = ('r', 'p', 's')

while True:
    user = input('Rock, paper, or scissors? (r,p,s): ').lower()
    if user not in choices:
        print('Invalid choice!')
        continue

    computer = random.choice(choices)

    print(f'You chose {emojis[user]}')
    print(f'Computer chose {emojis[computer]}')

    if user == computer:
        print('Tie')
    elif(
        (user == 'r' and computer == 's') or
        (user =='s' and computer == 'p') or
        (user == 'p' and computer =='r')):
        print('You win')
    else:
        print('You lose')

    proceed = input('Continue? (y/n): ').lower()
    if proceed == 'n':
        print('Thanks for playing!')
        break