choice = "y"

def total(qty,price):
    total_1 = qty * price

    if total_1 > 10000:
        discount_amount = total_1 * .10
        total_1 = total_1 - discount_amount
    return total_1

while choice == "y":
    qty = float(input("Enter quantity: "))
    price = float(input("Enter price: "))
    total_1 = total(qty, price)

    choice = input("Do you want to enter another item? ")
    print("Quantity: {} Price: {} Total: {}".format(qty, price, total_1))