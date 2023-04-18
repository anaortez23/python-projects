def main():
    print("Hello there")
    print("You can order Shamwowzers online now!")
    userInput = int(input("How many would you like to order: "))
    product, shipping, total = calculate(userInput)
    print('Shamwowzers ordered:', userInput)
    print('Subtotal:', product)
    print('Shipping Cost:', shipping)
    print('Total:', total)


def calculate(userInput):
    productsCost = userInput * 12.99
    shippingCost = round(userInput * 2.99, 2)
    totalCost = productsCost + shippingCost
    return productsCost, shippingCost, totalCost


main()
