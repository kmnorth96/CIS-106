def batting_average(hits, at_bats):
    batt_av = round(hits / at_bats, 3)
    return batt_av

ans = "y"
count = 0
while ans == "y":
    count += 1
    last_name = input("Enter players last name: ")
    hits = float(input("Enter number of hits: "))
    at_bats = float(input("Enter number of at bats: "))

    batt_av = batting_average(hits, at_bats)

    print("Last Name: {}\nBatting Average: {}".format(last_name, batt_av))
    print("Players Entered: ", count)

    ans = input("Do you want to continue?(y/n) ")