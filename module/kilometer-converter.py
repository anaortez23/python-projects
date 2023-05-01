
def kmToMilesConverter():
    calculate()

def calculate():
    km = int(input("Enter Km to convert to miles: "))
    miles = km * 0.6214
    print(km, "kilometers =", miles, "miles")


kmToMilesConverter()
