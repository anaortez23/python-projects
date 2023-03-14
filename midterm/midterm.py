import random
stop = False
userMoney = 0
matchedWords = 0
earnedMoney = 0

while stop == False:
    randomWord = random.randint(1, 3)
    """print(randomWord)"""
    userMoney = int(input("How much money do you want to insert?: "))
    print("Credit $", userMoney)
    if randomWord == 1:
        print("Your word: Cherries")
    elif randomWord == 2:
        print("Your word: Oranges")
    else:
        print("Your word: Plums")
    stop = True

for i in range(0, 3):
    randomDraw = random.randint(1, 3)
    if randomDraw == 1:
        print("Cherries")
        if randomDraw == randomWord:
            matchedWords = matchedWords + 1
    elif randomDraw == 2:
        print("Oranges")
        if randomDraw == randomWord:
            matchedWords = matchedWords + 1
    else:
        print("Plums")
        if randomDraw == randomWord:
            matchedWords = matchedWords + 1

print("Total matches: ", matchedWords)

if matchedWords <= 0 or matchedWords == 1:
    print("You won $0 dollars")

elif matchedWords == 2:
    earnedMoney = userMoney * 2
    print("You won: $", earnedMoney)
    print("New Credit: $", earnedMoney + userMoney)

elif matchedWords == 3:
    earnedMoney = userMoney * 3
    print("You won: $", earnedMoney)
    print("New Credit: $", earnedMoney + userMoney)
