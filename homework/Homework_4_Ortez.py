
def main():
    wallToPaint = int(input('Enter the square feet of the wall you want to paint:'))
    pricePerGallon = int(input('Enter the price per gallon of the paint:'))
    calculate(wallToPaint, pricePerGallon)


def calculate(sqFt, price):
    paintGallons = sqFt / 115
    laborRequired = paintGallons / 8
    laborCost = laborRequired * 8
    paintCost = paintGallons * price
    totalCost = laborCost + paintCost
    print('Number of gallons of paint required: ', round(paintGallons, 2))
    print('Hours of labor required: ', round(laborRequired, 2))
    print('Total cost of the paint: ', round(paintCost, 2))
    print('Labor charges are: ', round(laborCost, 2))
    print('Total cost of the paint job: ', round(totalCost, 2))


main()
