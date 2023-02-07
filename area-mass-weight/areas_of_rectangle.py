

recLength1 = int(input('Enter the length of the first rectangle:'))
recWidth1 = int(input('Enter the width of the first rectangle:'))
recLength2 = int(input('Enter the length of the second rectangle:'))
recWidth2 = int(input('Enter the width of the second rectangle:'))
recArea1 = recLength1 * recWidth1
recArea2 = recLength2 * recWidth2

print('The area of the first rectangle is',  recArea1)
print('The area of the second rectangle is',  recArea2)

if recArea1 > recArea2:
    print('The area of the first rectangle is bigger')
elif recArea1 < recArea2:
    print('The area of the second rectangle is bigger')
else:
    print('Both rectangles have the same area')
