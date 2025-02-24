principle = float(input("Enter principle amount of CD: "))
years = float(input("Enter how many years to CD maturity: "))

if principle > 100000 and years == 5:
    interest_rate = .06
elif principle >= 50000 and principle <= 100000 and years == 10:
    interest_rate = .05
elif principle >= 50000 and principle <= 100000 and years == 5:
    interest_rate = .04
else:
    interest_rate = .02

first_year = principle * interest_rate

print("Principle: {:.2f}\nInterest Rate: {:.2f}\nInterest in first year: {:.2f}".format(principle, interest_rate, first_year))