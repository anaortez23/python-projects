
weight = float(input('Enter your package weight:'))
1
if weight <= 2:
    shippingCost = float(weight * 1.10)
    print('Your shipping charge is:', shippingCost)
elif 2 < weight <= 6:
    shippingCost = float(weight * 2.20)
    print('Your shipping charge is:', shippingCost)
elif 6 < weight <= 10:
    shippingCost = float(weight * 3.70)
    print('Your shipping charge is:', shippingCost)
else:
    shippingCost = float(weight * 3.80)
    print('Your shipping charge is:', shippingCost)
