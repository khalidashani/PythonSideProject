# Computer choose one mumber
# Create guess function
# If high, say too hight
# If low, say too low
# If correct say congrats and break the loop

import random

number = random.randint(1, 1000)

while True:
    try:
        user = input("Guess the number between 1:1000:")
        guess = int(user)

        if guess > number:
            print('Too high. Try again')
        elif guess < number:
            print('Too low. Try again')
        else:
            print('You are correct. Thanks for playing')
            break
        
    except ValueError:
        print("Invalid value. Please enter number")
