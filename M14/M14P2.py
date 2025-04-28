class Student:
    def __init__(self, first, last, code, credits):
        self.first = first
        self.last = last
        self.code = code
        self.credits =  credits
    def tuition_owed(self):
        if self.code == 'I':
            balance = self.credits * 250.00
        else:
            balance = self.credits * 500.00
        return balance

student1 = Student('Keaton', 'Northcott', 'I', 12.0)

print(student1.first)
print(student1.last)
print(student1.tuition_owed())
