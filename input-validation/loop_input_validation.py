
score = int(input("Enter a test score: "))

while score < 0 or score > 100:
    print("Invalid")
    score = int(input("Enter a test score: "))
