last_names = ["Northcott", "Perez", "Fouts", "Farr", "Johnson", "Kennedy", "Mclaughlin", "Patel", "Solka", "Hanson"]
exam_scores = [100, 90, 75, 60, 80, 100, 100, 50, 90, 80]

def display_forward(names, scores):
    print("Last names and scores in order: ")
    for i in range(len(names)):
        print("{} - Score: {}".format(names[i], scores[i]))

def display_reverse(names, scores):
    print("\nLast names and scores in reverse order: ")
    for i in range(len(names)-1, -1, -1):
        print("{} - Score: {}".format(names[i], scores[i]))

display_forward(last_names, exam_scores)

display_reverse(last_names, exam_scores)