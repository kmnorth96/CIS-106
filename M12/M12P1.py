last_names = ["Northcott", "Perez", "Fouts", "Farr", "Johnson", "Kennedy", "Mclaughlin", "Patel", "Solka", "Hanson"]

def display_forward(last_names):
    print("Last names in order: ")
    for names in last_names:
        print(names)

def display_reverse(last_names):
    print("\nLast names in reverse order: ")
    for names in reversed(last_names):
        print(names)

display_forward(last_names)

display_reverse(last_names)