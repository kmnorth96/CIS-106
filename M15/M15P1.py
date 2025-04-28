class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@spaceX.com'

    def bonus(self, rate):
        b = float(rate) * float(self.pay)
        return b
    
class Manager(Employee):
    def long_term_bonus(self):
        return self.pay * .40
    
employee1 = Employee('Keaton', 'Northcott', 100000.00)
employee2 = Employee('Kylee', 'Northcott', 80000.00)

manager1 = Manager('Jeff', 'Bezos', 1000000000.00)
manager2 = Manager('Ada', 'Lovelace', 500000000.00)

print("{} {} | Email: {} | Pay: ${:.2f}".format(employee1.first, employee1.last, employee1.email, employee1.pay))
print("Bonus 10%: ${:.2f}, Bonus 20%: ${:.2f}\n".format(employee1.bonus(0.10), employee1.bonus(0.20)))

print("{} {} | Email: {} | Pay: ${:.2f}".format(employee2.first, employee2.last, employee2.email, employee2.pay))
print("Bonus 10%: ${:.2f}, Bonus 20%: ${:.2f}\n".format(employee2.bonus(0.10), employee2.bonus(0.20)))

print("{} {} | Email: {} | Pay: ${:.2f}".format(manager1.first, manager1.last, manager1.email, manager1.pay))
print("Long Term Bonus: ${:.2f}\n".format(manager1.long_term_bonus()))

print("{} {} | Email: {} | Pay: ${:.2f}".format(manager2.first, manager2.last, manager2.email, manager2.pay))
print("Long Term Bonus: ${:.2f}\n".format(manager2.long_term_bonus()))