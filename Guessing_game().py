from asyncore import loop
from random import random


def Guessing_game():
    num = random.randint(1, 200)
    guesses = 0
    while guesses <10:
        guess = int(raw_input("Enter an intger from 1 to 200"))
        print("this is you % guess")

        if guess < num:
            print("guess to low")
        elif guess > num:
            print("guess to high")
        elif guess == num:
            break    
        if guess == num:
            guesses = str(guesses)
            print("you guess " + str(100 * guesses / num) + "%")