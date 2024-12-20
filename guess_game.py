
# Number guessing game in python 

import random 
number = random.randint(1,9)
guess = 0
# tries = int(input('How many tries do you need ?'))   future update
chance = 1

try:
    while chance <= 3:
        print (f'\n{chance}/3 Tries\n')
        guess  = int(input('Enter your guess(0-9): '))
        if guess < 0 or guess > 9:
            print('INVALID INPUT ! Plz enter number between 0 - 9')
            break
        else:
            if guess == number:
                print(f'\nYou did it ! The number was {number}\n')
                break
            else:
                if chance < 3:
                    print('Try again !')
            chance +=1

    if chance > 3:
        print('You are out to tries !')
except ValueError:
    print('INVALID INPUT ! Plz enter integer ')
