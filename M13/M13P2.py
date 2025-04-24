student_grade = { "Keaton": [88, 90, 82],
                "Joe": [70, 65, 80],
                "Tommy": [85, 82, 94],
                "Crosley": [55, 60, 65]
                }

def calc_student(grade_dictionary):
    averages = []
    for name in grade_dictionary:
        grades = grade_dictionary[name]
        total = sum(grades)
        average = total / len(grades)
        averages.append([name, average])
    return averages

def calc_class(grade_dictionary):
    grade1 = 0
    grade2 = 0
    grade3 = 0
    num_students = len(grade_dictionary)

    for grades in grade_dictionary.values():
        grade1 += grades[0]
        grade2 += grades[1]
        grade3 += grades[2]

    grade1_avg = grade1 / num_students
    grade2_avg = grade2 / num_students
    grade3_avg = grade3 / num_students

    return [grade1_avg, grade2_avg, grade3_avg]


student_averages = calc_student(student_grade)
class_average = calc_class(student_grade)

print("{:<12} {:<6}".format("Name", "Average"))
print("-" * 20)

for item in student_averages:
    print("{:<13} {:.2f}".format(item[0], item[1]))

print("\nClass Average for Each Grade")
print("-" * 20)
print("First Grade Avg: {:.2f}".format(class_average[0]))
print("Second Grade Avg: {:.2f}".format(class_average[1]))
print("Third Grade Avg: {:.2f}".format(class_average[2]))