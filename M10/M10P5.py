def assessed_value(county, market_value):
    if county == "cook":
        percent = .90
    elif county == "dupage":
        percent = .80
    elif county == "mchenry":
        percent = .75
    elif county == "kane":
        percent = .60
    else:
        percent = .70

    total_assessed = market_value * percent
    return total_assessed



choice = "yes"
total_values = 0
market = 0

while choice == "yes":

    county = input("Enter county name: ").lower()
    market_value = float(input("Enter market value: "))

    total =  assessed_value(county, market_value)

    print("Assessed value is: ${:.2f}".format(total))

    total_values += total
    market += market_value

    choice = input("Do you want to run the program again?(yes/no)").lower()

print("Total of all market values: $",market)
print("Total of all assessed values: $",total_values)