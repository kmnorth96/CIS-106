def discount_amount(qty, price, discount_rate):
    to_be_discounted = qty * price
    discounted_total = to_be_discounted * discount_rate
    discounted_price = to_be_discounted - discounted_total
    return discounted_total, discounted_price

qty = float(input("Enter quantity: "))
price = float(input("Enter price: "))
discount_rate = float(input("Enter discount rate as a decimal: "))
discounted_total, discounted_price = discount_amount(qty, price, discount_rate)
print("Quantity: {:.2f}\nPrice: {:.2f}\nDiscount Amount: {:.2f}\nDiscount Price: {:.2f}".format(qty, price, discounted_total, discounted_price))