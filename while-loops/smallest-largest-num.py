
num = int(input('Enter a number:'))
if num != -99:

    greater = num
    smaller = num

while num != -99:
    num = int(input('Enter a number:'))
    if num != -99:
        if num > greater:
            greater = num
        if num < smaller:
            smaller = num

print('Smallest number is:', smaller, 'Greater number is:', greater)

"""
num = int(input('Enter a number:'))
if num != -99:
    small = num
    large = num

while num != -99:
    num = int(input('Enter a number:'))
    if num != -99:
        if large < num:
            large = num
        if small > num:
            small = num
print('Smallest number is:', small, 'Greater number is:', large)
"""
