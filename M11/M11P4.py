def average_score(score_1, score_2, score_3, handicap):
    average = (score_1 + score_2 + score_3) / 3 
    score_with_handicap = average + handicap
    return average, score_with_handicap

last_name = input("Enter bowlers last name: ")
score_1 = float(input("Enter game 1 score: "))
score_2 = float(input("Enter game 2 score: "))
score_3 = float(input("Enter game 3 score: "))
handicap = float(input("Enter handicap: "))

average, handicap_score = average_score(score_1, score_2, score_3, handicap)

print("Bowler: {}\nAverage: {:.0f}\nAverage with handicap: {:.0f}".format(last_name, average, handicap_score))