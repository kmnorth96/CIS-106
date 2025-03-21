def forecast(month, sales):
    if month in  ["jan", "feb", "mar"]:
        percent = .10
    elif month in ["apr", "may", "jun"]:
        percent = .15
    elif month in ["jul", "aug", "sep"]:
        percent = .20
    else:
        percent = .25
    next_month_sales = sales * (1 + percent)
    return next_month_sales

choice = "yes"

while choice == "yes":
    last_name = input("Enter user last name: ")
    month = input("Enter month as 3 letter abbreviation(jan, feb, mar): ").lower()
    sales = float(input("Enter sales: "))

    next =  forecast(month, sales)

    print("Next months estimated sales: {:.2f}".format(next))

    choice = input("Do you want to run the program again?(yes/no)").lower()