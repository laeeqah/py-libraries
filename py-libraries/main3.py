#Task 1

import random

random = random.randint(1,101)
chances= 0


while True:
    user_input=int(input("Put in your number: "))

    if user_input == random:
        print("Good Job")
        print("Number of guesses", chances)
        exit()

    elif user_input < random:
        print("Too Low")
        chances = chances + 1


    elif user_input > random:
        print("Too High")
        chances = chances + 1




