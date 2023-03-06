import random
stop = False
guesses = 0

while stop == False:
    num = random.randint(1, 6)
    """print(num)"""
    userGuess = int(input("The dice has rolled what's your guess?: "))
    guesses = guesses + 1
    if userGuess > num:
        print("Woops too high!!")
    elif userGuess < num:
        print("Aww too low!")
    else:
        print("You guessed the number in", guesses, "attempts!!")
        stop = True
