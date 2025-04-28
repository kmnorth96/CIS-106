class Student:
    #rates
    tuition_rates = {
        'I': 250.00, #in dist
        'O': 500.00, #out of dist
        'X': 800.00, #international
        'G': 250.00 #recip
    }
    #constructor
    def __init__(self, first, last, code, credits):
        self.first = first
        self.last = last
        self.code = code
        self.credits =  credits


    def tuition_owed(self):
        rate = Student.tuition_rates.get(self.code)
        balance = self.credits * rate
        return balance

student1 = Student('Kylee', 'Northcott', 'I', 12.0)
student2 = Student('Keaton', 'Northcott', 'O', 12.0)
student3 = Student('Shanelle', 'Northcott', 'X', 12.0)
student4 = Student('Michael', 'Northcott', 'G', 12.0)


print(student1.first, student1.last, student1.tuition_owed())
print(student2.first, student2.last, student2.tuition_owed())
print(student3.first, student3.last, student3.tuition_owed())
print(student4.first, student4.last, student4.tuition_owed())