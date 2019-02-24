

import random

secretNumber=random.randint(1,20)
print("I am thinking of a number from 1 to 20")
tries = 4

for guessesTaken in range(0,tries):
    print("Guess the number. You can try " + str(tries - guessesTaken) + " times.")
    guess=input()
    if not guess.isdigit():
            print("It is not a number. Try again")
    else:        
        guess=int(guess)
        if guess>secretNumber:
            print('Your guess is too high.')
        elif guess<secretNumber:    
            print('Your guess is too low')
        else:
            print('Your guess is correct, secret number is ', secretNumber)

            break
if guess==secretNumber:
    print('Your guess is correct, secret number is ', secretNumber)
else:
     print('Nope. The number I was thinking of was ' + str(secretNumber))
    
    
input()       
