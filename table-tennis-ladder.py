import random
import sys
from prettytable import PrettyTable


def get_players(filename):
    players_file = open(filename, "r")
    players_str = players_file.read()
    players = players_str.split(",")
    players_file.close()
    return players


def write_players(filename, players):
    players_file = open(filename, "w")
    write_str = ""
    for i in players:
        write_str = write_str + i + ","
    if write_str[0] == ",":
        write_str = write_str[1:]
    if write_str[len(write_str)-1] == ",":
        write_str = write_str[:len(write_str)-1]
    players_file.write(write_str)
    players_file.close()
    return


def get_ladder(filename):
    ladder_file = open(filename, "r")
    ladder_str = ladder_file.read()
    ladder = ladder_str.split(",")
    ladder_file.close()
    return ladder


def write_ladder(filename, ladder):
    ladder_file = open(filename, "w")
    write_str = ""
    for i in ladder:
        write_str = write_str + i + ","
    if write_str[0] == ",":
        write_str = write_str[1:]
    if write_str[len(write_str)-1] == ",":
        write_str = write_str[:len(write_str)-1]
    ladder_file.write(write_str)
    ladder_file.close()
    return


def match_played(winner, loser, ladder):
    if winner not in ladder:
        if loser not in ladder:
            ladder.append(winner)
            ladder.append(loser)
        else:
            loser_index = ladder.index(loser)
            ladder.insert(loser_index, winner)
    else:
        if loser not in ladder:
            ladder.append(loser)
        else:
            if ladder.index(winner) > ladder.index(loser):
                loser_index = ladder.index(loser)
                winner_index = ladder.index(winner)
                del ladder[winner_index]
                ladder.insert(loser_index, winner)
    return ladder


def view_leaderboard(ladder):

    print "--- LEADERBOARD ---"

    table = PrettyTable()

    table.field_names = ["Ranking", "Name"]

    for i in ladder:
        table.add_row([str(ladder.index(i)+1), i])
    print table


def enter_matches(players, ladder):
    while True:
        winner = str(raw_input("Please enter name of winner: "))
        if (winner not in players) or (winner.lower() not in [i.lower() for i in players]):
            print "Name not recognised. Please try again."
        else:
            break
    while True:
        loser = str(raw_input("Please enter name of loser: "))
        if loser not in players or loser.lower() not in [i.lower() for i in players]:
            print "Name not recognised. Please try again."
        else:
            break

    new_ladder = match_played(winner, loser, ladder)
    write_ladder("ladder.txt", new_ladder)

    print "-- Menu: Record matches --"
    print "1) Record another match"
    print "2) Return to main menu"

    user_choice = str(raw_input("Please select an option: "))

    while True:
        if user_choice == "1":
            enter_matches(players, ladder)
        elif user_choice == "2":
            main_menu(players, ladder)
        else:
            print "Input not recognised. Please try again."


def menu_leaderboard(players, ladder):
    view_leaderboard(ladder)

    print "-- Menu: Leaderboard --"
    print "1) Return to main menu"
    print "2) Exit program"

    user_choice = str(raw_input("Please select an option: "))

    while True:
        if user_choice == "1":
            main_menu(players, ladder)
        elif user_choice == "2":
            exit()
        else:
            print "Input not recognised. Please try again."
    

def menu_add_players(players, ladder):
    while True:
        player_name = str(raw_input("Please enter a name: "))
        if player_name in players or player_name.lower() in [i.lower() for i in players]:
            print "Player name already in use."
        else:
            players.append(player_name)
        user_fin = str(raw_input("Add more players? y/n: "))
        if user_fin == "n":
            write_players("players.txt", players)
            print ""
            main_menu(players, ladder)


def main_menu(players, ladder):
    players = get_players("players.txt")
    ladder = get_ladder("ladder.txt")
    print ""
    print "-- Menu --"
    print "1) Add players"
    print "2) Record a match"
    print "3) View leaderboard"
    print "4) Exit"

    user_choice = str(raw_input("Please select an option: "))

    if user_choice == "1" or user_choice == "1)":
        menu_add_players(players, ladder)

    elif user_choice == "2" or user_choice == "2)":
        enter_matches(players, ladder)

    elif user_choice == "3" or user_choice == "3)":
        menu_leaderboard(players, ladder)

    elif user_choice == "4" or user_choice == "4)":
        print "Goodbye!"
        exit()
    else:
        print "Invalid menu option selected."


def main():

    args = sys.argv[1:]
    players = get_players("players.txt")
    ladder = get_ladder("ladder.txt")

    if not args:
        main_menu(players, ladder)

    if args[0] == "--add":
        menu_add_players(players, ladder)

    elif args[0] == "--match":
        enter_matches(players, ladder)

    elif args[0] == "--view":
        menu_leaderboard(players, ladder)

    else:
        "Invalid argument provided."
        exit()


if __name__ == "__main__":
  main()
