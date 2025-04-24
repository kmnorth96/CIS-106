student_grade = { "Keaton": 88,
                "Joe": 70,
                "Tommy": 85,
                "Crosley": 55
                }

print("{:<12} {:<6}".format("Name", "Grade"))
print("-" * 20)

for name, grade in student_grade.items():
    print("{:<12} {:<6}".format(name, grade))

average = sum(student_grade.values()) / len(student_grade)
print("{:<12} {:<6}".format("Average", average))