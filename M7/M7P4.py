answer = input("Do you wish to continue the program? ")
count = 0
total_gross = 0

if answer == "Yes":
    print("Okay, let's continue")
    while answer == "Yes":
      last_name = input("Enter employee last name: ")
      hours = float(input("Enter hours worked: "))
      pay_rate = float(input("Enter pay rate: "))

      if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        gross_pay = (40 * pay_rate) + overtime_pay
      else:
        gross_pay = hours * pay_rate
    
      
      count = count + 1
      total_gross = total_gross + gross_pay
      average = total_gross / count
      print("Employee last name: {}\nGross pay: {:.2f}".format(last_name, gross_pay))
      answer = input("Do you wish to continue the program? ")

print("Number of employees: {}\nTotal Gross Pay: {:.2f}\nAverage Pay: {:.2f}".format(count, total_gross, average))