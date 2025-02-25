answer = input("Do you wish to continue this program?")
count = 0

if answer == "Yes":
    print("Okay, let's continue")
    
    while answer == "Yes":
        last_name = input("Enter last name: ")
        score = float(input("Enter first exam score: "))
        second_score = float(input("Enter second exam score: "))

        final_score = (score + second_score) / 2

        print("Final score for ", last_name, " is ", final_score)

        count = count + 1

        print("Number of students processed: ", count)

        answer = input("Do you wish to continue the program? ")