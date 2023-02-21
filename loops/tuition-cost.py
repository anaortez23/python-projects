count = 2
tuition = 12000
newTuition = 0

while count <= 5:
    cost = int(tuition + tuition * 0.02)
    newTuition = tuition + cost
    print(cost)
    count = count + 1
