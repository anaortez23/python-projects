total = 0
num = int(input('Enter a number:'))

while num > 0:
    total = total + num
    num = int(input())
    num = int(input('Enter a number:'))

print(total)
