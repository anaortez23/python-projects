
item1 = float(input('Enter price for your first item:'));
item2 = float(input('Enter price for your second item:'));
item3 = float(input('Enter price for your third item:'));
item4 = float(input('Enter price for your fourth item:'));

tax = 0.06
subTotal = item1 + item2 + item3 + item4;
salesTax = subTotal * tax;
total = subTotal + salesTax;

print('Your subtotal is:', str(round(subTotal, 2)),
      'Your sales tax is:', str(round(salesTax, 2)),
      'Your total is:', str(round(total, 2))
      );
