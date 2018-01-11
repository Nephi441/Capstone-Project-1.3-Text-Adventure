import random
import time
import sys
def fight_beast():
    fdmg1 = int(random.randint(1,7))
    edmg1 = int(random.randint(1,6))
    print("you hit a", fdmg1)
    print("the beast hits a ", edmg1)
    time.sleep(1)
    if edmg1 > fdmg1:
        print("you died")
    elif edmg1 < fdmg1:
         print("you killed the beast")
    else:
        print("you didnt kill the beast but you managed to escape")
        
def goguess():
    print('I have a number between 1 and 20 inclusive. Can you guess it?')
    number = random.randint(1,20)
    guess = int(raw_input())
    tries = 1
    while guess != number and tries < 6:
        tries += 1
        if guess<number:
            print(guess, 'is too low, guess again')
        else:
            print(guess, 'is too high')
        guess = int(raw_input())
    if guess == number:
        print('Right! You guessed in', tries, 'tries')