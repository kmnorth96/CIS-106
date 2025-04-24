def load_players(filename):
    player_dict = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            parts = line.split(",")
            name = parts[0]
            average = float(parts[1])
            player_dict[name] = average
    return player_dict

def print_players(player_dict):
    print("{:<12} {:<8}".format("Name", "Average"))
    print("----------------------")
    for name in player_dict:
        print("{:<12} {:.3f}".format(name, player_dict[name]))

players = load_players("players.txt")
print_players(players)

# player lookupp
while True:
    user_input = input("\nEnter player's last name to look up or type exit to quit: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    if user_input in players:
        print("Player: {:<12} Average: {:.3f}".format(user_input, players[user_input]))
    else:
        print("Player not found try again.")