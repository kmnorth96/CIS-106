#input item choice and quantity of items
item = input("Enter item A or B: ")
quantity = float(input("Enter quantity: "))
#determine unit price based on item input
if item == "A":
    unit_price = 10
else:
    unit_price = 20
#calculate extended price
ext_price = quantity * unit_price
#display item choice, unit price, and extended price
print("Item: {}".format(item))
print("Unit Price: ${}".format(unit_price))
print("Extended Price: ${}".format(ext_price))