

mealTotal = float(input('Enter the price of your meal: '));

tipCalc = mealTotal * 0.15
taxCalc = mealTotal * 0.06
totalMealCost = mealTotal + tipCalc + taxCalc

tippedMeal = print('Sales tax is: $',taxCalc,", "
                   '15% tip is: $',tipCalc,", "
                   'Total is: $',totalMealCost);
