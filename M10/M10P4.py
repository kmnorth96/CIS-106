def ticket_price(miles):
    if miles >= 30:
        price = 12
    elif miles >= 20:
        price = 10
    elif miles >= 10:
        price = 8
    else:
        price = 5
    return price

choice = "yes"
all_tickets = 0

while choice == "yes":

    last_name = input("Enter last name: ").lower()
    miles_from_chicago = float(input("Enter miles from Chicago: "))

    total =  ticket_price(miles_from_chicago)

    print("Ticket price for {} is: ${}".format(last_name, total))

    all_tickets += total

    choice = input("Do you want to run the program again?(yes/no)").lower()

print("Total of all tickets: $",all_tickets)