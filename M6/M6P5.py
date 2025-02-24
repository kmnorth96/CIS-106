last_name = input("Enter employee last name: ")
salary = float(input("Enter employee salary: "))
job_level = float(input("Enter job level: "))

if job_level >= 10:
    bonus_rate = .25
elif job_level >= 5 and job_level < 10:
    bonus_rate = .20
else:
    bonus_rate = .10

bonus = salary * bonus_rate

print("{}\nBonus: {}".format(last_name, bonus))