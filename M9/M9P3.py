def mpg(miles, gallons):
    return round(miles / gallons, 2)

choice = "y"
count = 0
while choice == "y":
    count += 1
    destination = input("Enter destination city: ")
    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))

    miles_per = mpg(miles, gallons)
    choice = input("Do you wish to enter another trip?(y/n) ")
    print("Destination: {}\nMiles: {}\nMPG: {}".format(destination, miles, miles_per))