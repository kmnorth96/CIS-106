#create input for required parameters
last_name = input("Enter user's last name: ")
dependants = float(input("Enter number of dependants: "))
gross_income = float(input("Enter gross income: "))
#calculate adjusted gross income
adjusted_gross = gross_income - (dependants * 12000)
#condition to check adjusted gross income to determine tax rate
if adjusted_gross > 50000:
    tax_rate = .20
else:
    tax_rate = .10
#calculate income tax
income_tax = adjusted_gross * tax_rate
#condition if income tax is less than 0, set it to 100 
if income_tax < 0:
    income_tax = 100
#display last name, gross income, dependants, adjusted gross income, and income tax
print("Last name: {}".format(last_name))
print("Gross income: ${:.2f}".format(gross_income))
print("Dependants: {}".format(dependants))
print("Adjusted Gross Income: {:.2f}".format(adjusted_gross))
print("Income Tax: {:.2f}".format(income_tax))