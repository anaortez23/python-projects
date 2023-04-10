MARK_UP = 2.5


def main():
    another = "y"
    while another.lower() == "y":
        showRetail()
        choice = input("Enter y if you want to continue: ")


def showRetail():
    wholesale = float(input("Enter the item's wholesale cost: "))
    while wholesale < 0:
        print("ERROR: the cost cannot be negative.")
        wholesale = float(input("Enter the correct wholesale cost:"))


main()
