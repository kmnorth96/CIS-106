last_names = ["Northcott", "Perez", "Fouts", "Farr", "Johnson", "Kennedy", "Mclaughlin", "Patel", "Solka", "Hanson"]
batting_avg = [.333, .200, .150, .352, .278, .190, .244, .282, .304, .296]

def display_players_avg(names, avg):
    print("Player Batting Averages: ")
    for i in range(len(names)):
        print("{} - {:.3f}".format(names[i], avg[i]))

def search(names, avg, player):
    found = False
    for i in range(len(names)):
        if names[i].lower() == player.lower():
            print("{}'s batting average is {:.3f}".format(names[i], avg[i]))
            found = True
            break
    if not found:
        print("Name not found.")

def main(): 
    display_players_avg(last_names, batting_avg)

    while True:
        name = input("\nEnter name you wish to search for or type quit to stop: ")
        if name.lower() == "quit":
            print("Quitting")
            break
        search(last_names, batting_avg, name)

main()