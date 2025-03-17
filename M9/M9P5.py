tuition = 0
def tuition_owed(credit_hours, district):
    if district == "I":
        credit = 250
    elif district == "O":
        credit = 550

    tuition = credit * credit_hours
    return tuition
total = 0

choice = "y"
while choice == "y":
    last_name = input("Enter students last name: ")
    credit_hours = float(input("Enter how many credit hours are being taken: "))
    district = input("Enter district code: ").upper()

    tuition = tuition_owed(credit_hours, district)

    print("Student Name: {}\nTuition Owed: {}".format(last_name, tuition))
    choice = input("Do you want to input another student?(y/n) ").lower()
    total += tuition

print("Total tuition owed: {}".format(total))