players = {}

file = open("players.txt", "r")

for line in file:

    data = line.strip().split()

    name = data[0]
    average = float(data[1])

    players[name] = average

file.close()

def display_players(player_dict):

    print("Player Name    Batting Average")
    print("------------------------------")

    for name in player_dict:
        print(f"{name:15} {player_dict[name]:.3f}")

display_players(players)
