flag = True
total = 0

while flag:
    num = int(input('Enter a number:'))
    if num > 0:
        total = total + num
    else:
        flag = False

print(total)
