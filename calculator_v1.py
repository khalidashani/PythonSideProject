# create calculator that can do addition and substraction

while True:
    # Float systax to convert the user input into int
    number1 = float(input("Input first number: "))
    number2 = float(input("Input second value: "))

    # could add error handling function should user enter character instead of number

    # could use 'a' for addition and 's' for substraction to ease user input
    operation = input("Choose operation (+/-): ")

    if operation == '-':
        print(number1 - number2)
    elif operation == '+':
        print(number1 + number2)
    else:
        print("Incorrect operation, choose again")

    proceed = input("Proceed (y/n): ").lower()

    if proceed == 'y':
        continue
    elif proceed == 'n':
        break
    else:
        print("Incorrection choice, choose again")
