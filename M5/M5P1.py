#input quantity to be purchased
quantity = float(input("Enter quantity of the item: "))
#determine unit price based on quantity purchased 
if quantity >= 1000: 
    unit_price = 3.00   
else: 
    unit_price = 5.00
#calculate extended price
ext_price = quantity * unit_price
#calculate tax
tax = ext_price * .07
#calculate total
total = ext_price + tax
#display quantity, unit price, extended price, tax, and total
print("Quantity:  {}".format(quantity))
print("Unit Price: ${:.2f}".format(unit_price))
print("Extended Price: ${:.2f}".format(ext_price))
print("Tax: ${:.2f}".format(tax))
print("Total: ${:.2f}".format(total))