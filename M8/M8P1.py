principle = float(input("Enter principal amount: "))
interest_rate = float(input("Enter interest rate as a decimal: "))

i = 1
total_interest = 0

print("Year\tBeginning Balance\tEnding Balance")

for year in range(1, 6):
    interest = principle * interest_rate
    ending_balance = principle + interest

    print("{}\t${:,.2f}\t${:,.2f}".format(year, principle, ending_balance))
    
    total_interest += interest
    principle = ending_balance

print("\nTotal interest earned: {:,.2f}".format(total_interest))