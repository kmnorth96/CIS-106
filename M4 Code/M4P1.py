exam_1 = input("Enter score from exam 1: ")
exam_2 = input("Enter score from exam 2: ")

exam_1_computed = float(exam_1) * 0.60
exam_2_computed = float(exam_2) * 0.40

total_score = exam_1_computed + exam_2_computed

print("Total score: {:.2f}".format(total_score))