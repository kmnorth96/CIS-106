quantity =float(input("Input quantity of widgets: "))

if quantity > 10000:
    price = 10
elif quantity > 5000 and quantity < 10000:
    price = 20
else:
    price = 30

extendedPrice = quantity * price
tax = extendedPrice * .07
total = tax + extendedPrice

print("Extended Price: {:.2f}\nTax amount: {:.2f}\nTotal: {:.2f}".format(extendedPrice, tax, total))