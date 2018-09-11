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


# moves or adds winner/loser to correct positions in ladder
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


# print leaderboard
def view_leaderboard(ladder):

    print "--- LEADERBOARD ---"

    table = PrettyTable()

    table.field_names = ["Ranking", "Name"]

    for i in ladder:
        table.add_row([str(ladder.index(i)+1), i])
    print table
    exit()


# record new match
def add_new_matches_list(matches, ladder):
    for i in range(0, len(matches)-1, 2):
        winner = matches[i]
        loser = matches[i+1]

        ladder = match_played(winner, loser, ladder)
        print "Match: " + str(winner) + " beating " + str(loser) + " has been recorded."
    write_ladder("ladder.txt", ladder)

    return ladder


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

    print ""
    print "-- Menu: Record matches --"
    print "1) Record another match"
    print "2) Return to main menu"

    user_choice = str(raw_input("Please select an option: "))

    while True:
        if user_choice == "1":
            enter_matches(players, ladder)
        elif user_choice == "2":
            main_menu()
        else:
            print "Input not recognised. Please try again."


# add new players (straight from command line)
def add_new_players_list(players, new_players):
    duplicate_players = []
    added_players = []

    for player_name in new_players:
        if player_name in players or player_name.lower() in [i.lower() for i in players]:
            duplicate_players.append(player_name)
        else:
            players.append(player_name)
            added_players.append(player_name)
    write_players("players.txt", players)

    if len(added_players) != 0:
        print "The following players were added successfully: " + ", ".join(added_players)
    if len(duplicate_players) != 0:
        print "The following players are already in the players list: " + ", ".join(duplicate_players)


# add new players (from menu option)
def menu_add_players(players):

    while True:
        player_name = str(raw_input("Please enter a name: "))
        if player_name in players or player_name.lower() in [i.lower() for i in players]:
            print "Player name already in use."
        else:
            players.append(player_name)
            print player_name + " added successfully!"
        user_fin = str(raw_input("Add more players? y/n: "))
        if user_fin == "n":
            write_players("players.txt", players)
            print ""
            main_menu()


# print menu, read in and act on user choice from menu
def main_menu():
    # re-read the players/ladders data - in essence, do a "refresh"
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
        menu_add_players(players)

    elif user_choice == "2" or user_choice == "2)":
        enter_matches(players, ladder)

    elif user_choice == "3" or user_choice == "3)":
        view_leaderboard(ladder)

    elif user_choice == "4" or user_choice == "4)":
        print "Goodbye!"
        exit()
    else:
        print "Invalid menu option selected."


def print_help():
    print "[--add] \t\t\t Brings up the 'add player' prompt menu.\n" \
          "[--add name1 name2...] \t\t Adds each specified player to the players list. Players already present in the list will not be added, and an alert will appear.\n" \
          "[--match] \t\t\t Brings up the 'record match' prompt menu.\n" \
          "[--match winner loser...] \t Records matches between two players. Multiple match records can be entered at once. No matches will be recorded if an odd number of players is specified.\n" \
          "[--view] \t\t\t Allows the viewing of the current leaderboard\n" \
          "[] \t\t\t\t Not specifying an argument will bring up the main menu.\n"


def main():

    # retrieve non-script arguments
    args = sys.argv[1:]

    # if no arguments have been given, send user to prompts menu
    if not args:
        main_menu()
    else:
        players = get_players("players.txt")
        ladder = get_ladder("ladder.txt")

        # "--add" argument specified
        if args[0] == "--add":
            # check whether names of players have been specified
            new_players = args[1:]
            if len(new_players) != 0:
                # proceed straight to adding players if names have been specified
                add_new_players_list(players, new_players)
            else:
                # send user to adding-specific prompts menu if no names specified
                menu_add_players(players)

        # "--match" argument specified
        elif args[0] == "--match":
            # check whether names of players have been specified
            new_matches = args[1:]
            if len(new_matches) != 0:
                # check whether an even number of players have been specified
                if len(new_matches) % 2 == 0:
                    add_new_matches_list(new_matches, ladder)
                else:
                    print "Odd number of players specified. Please try again."
            else:
                # send user to record-matches-specific prompts menu if no names specified
                enter_matches(players, ladder)

        # "--view" argument specified
        elif args[0] == "--view":
            # send user to leaderboard view
            view_leaderboard(ladder)

        # "--help" argument specified
        elif args[0] == "--help":
            # print helper function
            print_help()

        else:
            "Invalid argument provided."
            exit()


if __name__ == "__main__":
    main()
