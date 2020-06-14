#!/usr/bin/env/ python3
import random

# SECRET NUMBER GUESS
def guess_num():
    secret_num = random.randrange(10)
    attempts = 3
    while True:
        guess = input("Enter a guess for the secret number (0-9): ")

        if guess.isdigit() == True:
            if int(guess) < secret_num:
                print("\nWrong...! Guess is lower than the number, try again.")
            elif int(guess) == secret_num:
                print("\nCongrats! your Guess is right. The secret number is", secret_num)
                break
            elif int(guess) > secret_num:
                print("\nWrong...! Guess is higher than the number, try again.")    

            if attempts == 1:
                print('\n3 strikes... and you are out!\n The secret number is', secret_num)
                break
        else:
            print("\nInvalid: guess should only use digits")
        attempts -= 1

guess_num()       
        
        