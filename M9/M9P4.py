rate = 0
def pay_rate(job_code):
    if job_code == "L":
        rate = 25
    elif job_code == "A":
        rate = 30
    elif job_code == "J":
        rate = 50
    else:
        print("Incorrect job code!")
    return rate

choice = "y"
total = 0

while choice == "y":

    last_name = input("Enter employee last name: ")
    job_code = input("Enter job code: ").upper()
    hours = float(input("Enter hours worked: "))

    overtime_hours = hours - 40
    if overtime_hours > 40:
        overtime_pay = overtime_hours * (rate * 1.5)
    else: 
        overtime_pay = 0

    gross_pay = pay_rate(job_code) * hours + overtime_pay

    print("Last Name: {}\nGross Pay: {}".format(last_name, gross_pay))

    total += gross_pay
    
    choice = input("Do you want to add another employee?(y/n)").lower()

print("The total gross pay for entered employees: {}".format(total))