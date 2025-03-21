def out_the_door(msrp, model, code):
    if model == "accord":
        discount = .10
    elif model == "rav4":
        discount = .15
    elif code == "y":
        discount == .30
    else:
        discount = .05
    amount_off = msrp * discount
    tax_amount = (msrp - amount_off) * .07
    taxed_total = (msrp - amount_off) + tax_amount
    return taxed_total



choice = "yes"
all_msrp = 0
all_sales = 0

while choice == "yes":

    make = input("Enter make: ").lower()
    model = input("Enter model: ").lower()
    code = input("Enter electric vehicle code(Y or N): ").lower()
    msrp = float(input("Enter vehicle msrp: "))

    total =  out_the_door(msrp, model, code)

    print("Out the door price is: {:.2f}".format(total))

    all_msrp += msrp
    all_sales += total

    choice = input("Do you want to run the program again?(yes/no)").lower()

print("Total MSRP's is:", all_msrp)
print("Total out the door prices is:", all_sales)