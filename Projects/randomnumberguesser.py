import random

random_num = random.randint(1,10)

user_input = int(input("Enter your guess:"))

if user_input == random_num:
    print("Correct Guess")
else:
    print("Incorrect Guess")
