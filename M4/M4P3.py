meal_price = float(input("Enter total for the meal: "))

tip_15 = float(meal_price) * 0.15
tip_18 = float(meal_price) * 0.18
tip_20 = float(meal_price) * 0.20


total_15 = float(meal_price) + tip_15
total_18 = float(meal_price) + tip_18
total_20 = float(meal_price) + tip_20

print("With 15% tip: \n\nTotal: {:14.2f}\nTip: {:16.2f}\nTotal with Tip {:6.2f}\n\n".format(meal_price, tip_15, total_15))

print("With 18% tip: \n\nTotal: {:14.2f}\nTip: {:16.2f}\nTotal with Tip {:6.2f}\n\n".format(meal_price, tip_18, total_18))

print("With 20% tip: \n\nTotal: {:14.2f}\nTip: {:16.2f}\nTotal with Tip {:6.2f}".format(meal_price,tip_20, total_20))

