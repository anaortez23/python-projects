
def main():
    payRate = int(input("Enter pay rate: "))
    while payRate < 7.50 or payRate > 18.25:
        print("Invalid")
        payRate = int(input("Enter pay rate: "))

    hours = int(input("Enter hours worked: "))
    while hours < 0 or hours > 40:
        print("Invalid")
        hours = int(input("Enter hours worked: "))
    getGrossPay(payRate, hours)


def getGrossPay(payRate, hours):
    grossPay = payRate*hours
    print("Your gross pay is: ", grossPay)


main()
