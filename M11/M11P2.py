def average_and_total(score_1, score_2, score_3):
    total = score_1 + score_2 + score_3
    average = total / 3
    return total, average

last_name = input("Enter students last name: ")
score_1 = float(input("Enter exam 1 score: "))
score_2 = float(input("Enter exam 2 score: "))
score_3 = float(input("Enter exam 3 score: "))

total, average = average_and_total(score_1, score_2, score_3)
print("Last Name: {}\nTotal Points: {:.2f}\nAverage score: {:.2f}".format(last_name, total, average))