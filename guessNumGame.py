import random
print ('Hello, what is your name?')
name = input()
solved = False
while solved == False:
    secretNumber = random.randint(1,20)
    print ('Well, '+name+' I am thinking of a random number between 1 & 20')

    for guessesTaken in range(1,7):
        print('Take a guess')
        guess = int(input())
        if guess < secretNumber:
            print('Your guess is too low')
        elif guess > secretNumber:
            print('Your guess is too high')
        else:
            break

    if guess == secretNumber:
        solved = True
        print('Good job you guessed it!')
    else:
        print('Damn you suck')
