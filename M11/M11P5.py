total = 0
tax = 0

def compute_total(qty, price):
    global total, tax
    total = qty * price
    tax = total * .07

qty = float(input("Enter quantity: "))
price = float(input("Enter unit price: "))

compute_total(qty, price)

print("Total: {:.2f}\nTax: {:.2f}".format(total, tax))