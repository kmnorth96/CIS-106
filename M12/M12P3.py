high_var = 0
low_var = 999
high_ind = 0
low_ind = 0

last_names = ["Northcott", "Perez", "Fouts", "Farr", "Johnson", "Kennedy", "Mclaughlin", "Patel", "Solka", "Hanson"]
exam_scores = [100, 90, 75, 60, 80, 100, 100, 50, 90, 80]

for i in range(len(exam_scores)):
    if exam_scores[i] > high_var:
        high_var = exam_scores[i]
        high_ind = i
    if exam_scores[i] < low_var:
        low_var = exam_scores[i]
        low_ind = i

print("Highest Score: {} - {}".format(last_names[high_ind], high_var))
print("Lowest Score: {} - {}".format(last_names[low_ind], low_var))