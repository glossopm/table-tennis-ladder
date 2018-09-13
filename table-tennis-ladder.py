import sys
from prettytable import PrettyTable
import csv
import string


# ------------------------------------------READ/WRITE OPERATIONS------------------------------------------------------

# function to get a list from a .txt file
def get_list_file(filename):
    list_file = open(filename, "r")
    list_str = list_file.read()
    list_name = list_str.split(",")
    list_file.close()
    return list_name


# function to write a list to a .txt file
def write_list_file(filename, data):
    list_file = open(filename, "w")
    write_str = ""
    for i in data:
        write_str = write_str + i + ","
    write_str = write_str.rstrip(",").lstrip(",")
    list_file.write(write_str)
    list_file.close()


# read leaderboards order data from .txt file
def get_leaderboards():
    return get_list_file("default_lboard.txt")


# read players data from .txt file, store and return "players" list
def get_players():
    return get_list_file("players.txt")


# write leaderboards order data to .txt file
def write_lboards(data):
    return write_list_file("default_lboard.txt", data)


# write leaderboards order data to .txt file
def write_players(data):
    return write_list_file("players.txt", data)


# read leaderboards data from .csv file and store and return "leaderboards" dictionary
def get_lboards_dict():

    reader = csv.reader(open("leaderboards.csv", "r"))
    mydict = {}
    for row in reader:
        key, val = row
        if key not in mydict:
            temp = []
            temp.append(val)
            mydict[key] = temp
        else:
            temp = mydict[key]
            temp.append(val)
            mydict[key] = temp

    return mydict


def write_lboards_dict(lboard_dict):

    w = csv.writer(open("leaderboards.csv", "w"))

    for key in lboard_dict:
        for i in lboard_dict[key]:
            w.writerow([key, i])


def get_data():
    return get_leaderboards(), get_players(), get_lboards_dict()

# ------------------------------------------WRITE HTML FILE OPERATIONS--------------------------------------------------

def create_html_file(lboards_dict):

    html_string = ""

    html_string = "<!DOCTYPE html><br>"
    html_string = html_string + """<html>\n<head>\n<style>
    body {
      background-color: ivory;
      allign: center;
      display: block;
      margin-left: auto;
      margin-right: auto; 
    }
    h1  {
      color: blue;
    }
    #wrapper { 
       width: 1000px; 
       margin: 0 auto; 
    }
    table, th, td {
    border: 1px solid black;
    text-align: center;
    border-spacing: 5px;
    }
    p  {
      color: red;
    }
   </style>"""
    html_string = html_string + "<title> Table-Tennis Leaderboards</title>\n</head>\n <h1> Table-Tennis Leaderboards </h1>"
    html_string = html_string + "<body id=\"wrapper\">\n"

    for i in lboards_dict:
        table = PrettyTable()
        table.field_names = ["Ranking", "Name"]
        #print i
        html_string = html_string + i + "<br>"

        for j in lboards_dict[i]:
            #print j
            table.add_row([str(lboards_dict[i].index(j)+1), str(j)])

        html_string = html_string + "<table border: 1px solid black>" +table.get_html_string() +"</table>"
        html_string = html_string + "<br><br>"

    html_string = html_string + "</body>\n"
    html_string = html_string + "</html>"
    html_file = open("lboards_html.html", "w+")

    html_file.write(html_string)
    html_file.close()

# ------------------------------------------ADD PLAYERS FUNCTIONS------------------------------------------------------

# add new players (straight from command line)
def add_new_players_list(players, new_players):
    duplicate_players = []
    added_players = []
    failed_players = []

    for player_name in new_players:
        if player_name in players or player_name.lower() in [i.lower() for i in players]:
            duplicate_players.append(player_name)
        else:
            if not player_name.isalpha():
                failed_players.append(player_name)
            else:
                players.append(player_name.strip("\n"))
                added_players.append(player_name)
    write_players(players)

    if len(added_players) != 0:
        print "The following players were added successfully: " + ", ".join(added_players)
    if len(duplicate_players) != 0:
        print "The following players are already in the players list: " + ", ".join(duplicate_players)
    if len(failed_players) != 0:
        print "Adding the following players failed - please check names and try again: " + ", ".join(failed_players)


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
            write_players(players)
            print ""
            main_menu()


# ------------------------------------------RECORD MATCH FUNCTIONS-----------------------------------------------------

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


# record new match (from prompt menu)
def enter_matches(players, default_lboard, lboards_dict):
    ladder = lboards_dict[default_lboard]
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

    if winner == loser:
        print "Players' names must be unique. Please try again."
        main_menu()

    new_ladder = match_played(winner, loser, ladder)
    lboards_dict[default_lboard] = new_ladder
    write_lboards_dict(lboards_dict)

    user_choice = display_record_matches_menu()

    while True:
        if user_choice == "1":
            enter_matches(players, ladder, lboards_dict)
        elif user_choice == "2":
            main_menu()
        else:
            print "Input not recognised. Please try again."


# add a match for a leaderboard - "players" and "lboard" both list format
def enter_lboard_match(players, matches, lboard):

    duplicate_players = []
    failed_records = []
    new_lboard = lboard

    for i in range(0, len(matches)-1, 2):
        winner = matches[i]
        loser = matches[i+1]

        if winner == loser:
            duplicate_players.append(winner)
        else:
            if winner not in players or (winner.lower() not in [i.lower() for i in players]):
                failed_records.append((winner, loser))
            elif loser not in players or (loser.lower() not in [i.lower() for i in players]):
                failed_records.append((winner, loser))
            else:
                new_lboard = match_played(winner, loser, new_lboard)
                print "Match: " + str(winner) + " beating " + str(loser) + " has been recorded."

    for i in failed_records:
        print "Match: " + str(i[0]) + " beating " + str(i[1]) + " not recorded - one or both players missing from players list."

    for i in duplicate_players:
        print "Match for player " + str(i) + " not recorded - players cannot play against themselves"

    return new_lboard


# ------------------------------------------CHANGE LEADERBOARD FUNCTIONS------------------------------------------------

# change leaderboard from command line
def change_lboard(lboardsDict, args):
    if not args[1] or args[1] not in lboardsDict:
        print "Error: leaderboards does not exist. Record a match to create a new leaderboard."
    else:
        # removes new_name from list wherever it is then adds it to the front to become the default leaderboard
        new_name = args[1]
        print "The current leaderboard is now '" + new_name + "'."

    write_lboards(new_name)
    write_lboards_dict(lboardsDict)


# ------------------------------------------VIEW LEADERBOARD FUNCTIONS--------------------------------------------------

# print leaderboard
def view_leaderboard(lboard_name, ladder):

    table = PrettyTable()
    table.field_names = ["Ranking", "Name"]

    for i in ladder:
        table.add_row([str(ladder.index(i)+1), str(i)])
    print "--- " + lboard_name.upper() + " ---"
    print table
    exit()


# ------------------------------------------VIEW PLAYERS FUNCTIONS------------------------------------------------------

# print players
def view_players(players):

    table = PrettyTable()
    table.field_names = ["Name"]

    for i in players:
        if i.isspace() == False or i.isspace() != "":
            table.add_row([i])
    print "--- PLAYERS ---"
    print table
    exit()


# ------------------------------------------SEARCH PLAYERS FUNCTIONS----------------------------------------------------

# search function returns position of player
def search_players(lboard_name, search_terms, ladder):
    for i in search_terms:
        if i in ladder:
            print i + " is ranked position " + str(ladder.index(i) + 1) + " in leaderboard '" + str(lboard_name) + "'."
        else:
            print i + " is unranked in leaderboard '" + str(lboard_name) + "'."


# search function returns position of player
def search_players_menu(ladder):
    while True:
        search_term = str(raw_input(("Please enter a player to search for: ")))

        if search_term in ladder:
            print search_term + " is ranked position " + str(ladder.index(search_term) + 1) + "."
        else:
            print search_term + " is unranked."

        user_fin = str(raw_input("Search for another player? y/n: "))
        if user_fin == "n":
            exit()

# ------------------------------------------PLAY MATCH FUNCTION --------------------------------------------------------
def match_choice(args, players, lboardOrder,lboards_dict):

    # if players and leaderboard aren't specified, send user to prompts menu
    if len(args) == 1:
        print "ERROR: No names specificed. See --help for details.\n"
        print_help()
        exit()

    first_arg = args[1]
    # if leaderboard is specified
    if first_arg.startswith("--"):
        lboard = first_arg[2:]
        matches = args[2:]
        # if leaderboard is specified and players are specified, check number of players
        if matches:
            # if number of players is even, send user to leaderboard-specific match entry menu
            if len(matches) % 2 == 0:
                if lboard not in lboards_dict:
                    lboard_param = []
                else:
                    lboard_param = lboards_dict[lboard]
                new_lboard = enter_lboard_match(players, matches, lboard_param)
                lboards_dict[lboard] = new_lboard
                write_lboards_dict(lboards_dict)
                create_html_file(lboards_dict)
            # if number of players is odd, provide user with error
            else:
                print "ERROR: odd number of players provided."
        # if leaderboard is specified and players aren't, give user an error
        else:
            print "ERROR: please enter player names"
    else:
        print lboardOrder[0]
        lboard = lboardOrder[0]
        matches = args[1:]
        # if leaderboard is specified and players are specified, check number of players
        if matches:
            # if number of players is even, send user to leaderboard-specific match entry menu
            if len(matches) % 2 == 0:
                new_lboard = enter_lboard_match(players, matches, lboards_dict[lboard])
                lboards_dict[lboard] = new_lboard
                write_lboards_dict(lboards_dict)
                create_html_file(lboards_dict)
            # if number of players is odd, provide user with error
            else:
                print "ERROR: odd number of players provided."
        # if leaderboard is specified and players aren't, give user an error
        else:
            print "ERROR: please enter player names"


# ------------------------------------------DISPLAY MENU FUNCTIONS------------------------------------------------------

# print the matches-specific context menu
def display_record_matches_menu():
    print ""
    print "-- Menu: Record matches --"
    print "1) Record another match"
    print "2) Return to main menu"

    user_choice = str(raw_input("Please select an option: "))

    return user_choice


# ------------------------------------------MAIN MENU FUNCTIONS---------------------------------------------------------

# print menu, read in and act on user choice from menu
def main_menu():
    # re-read the players/ladders data - in essence, do a "refresh"

    lboards_order, players, lboards_dict = get_data()

    default_lb_name = lboards_order[0]

    print ""
    print "-- Menu --"
    print "1) Add players"
    print "2) Record a match"
    print "3) View leaderboard"
    print "4) View players"
    print "5) Search player"
    print "6) Exit"

    user_choice = str(raw_input("Please select an option: "))

    # strips off the ")" character if a user types e.g. "3)" instead of "3" for view leaderboard
    user_choice = user_choice.replace(")","")

    if user_choice == "1":
        menu_add_players(players)

    elif user_choice == "2":
        enter_matches(players, default_lb_name, lboards_dict)

    elif user_choice == "3":
        view_leaderboard(default_lb_name, lboards_dict[default_lb_name])

    elif user_choice == "4":
        view_players(players)

    elif user_choice == "5":
        search_players_menu(default_lb_name)

    elif user_choice == "6":
        print "Goodbye!"
        exit()
    else:
        print "Invalid menu option selected."


# print helper function
def print_help():
    print "[--add] \t\t\t Brings up the 'add player' prompt menu.\n" \
          "[--add name1 name2...] \t\t Adds each specified player to the players list. Players already present in the list will not be added, and an alert will appear.\n" \
          "[--match] \t\t\t Error: please specify a winner and loser.\n" \
          "[--match winner loser...] \t Records matches between two players. Multiple match records can be entered at once. No matches will be recorded if an odd number of players is specified.\n" \
          "[--view] \t\t\t Allows the viewing of the current leaderboard\n" \
          "[--players] \t\t\t Allows the viewing of the full list of players\n" \
          "[] \t\t\t\t Not specifying an argument will bring up the main menu.\n"


# main - entry point of program
def main():

    # retrieve non-script arguments
    args = sys.argv[1:]

    # if no arguments have been given, send user to prompts menu
    if not args:
        main_menu()
    else:
        lboardOrder, players, lboards_dict = get_data()
        # "--add" argument specified
        if args[0] == "--add":
            # check whether names of players have been specified
            new_players = args[1:]
            if len(new_players) != 0:
                # proceed straight to adding players if names have been specified
                add_new_players_list(players, new_players)
            else:
                # send user to help screen.
                print "ERROR: No names specified. See --help below for details.\n"
                print_help()

        # "--match" argument specified
        elif args[0] == "--match":
            match_choice(args, players, lboardOrder,lboards_dict)
            

        # "--view" argument specified
        elif args[0] == "--view":
            # send user to default leaderboard view
            if len(args) == 1:
                view_leaderboard(lboardOrder[0], lboards_dict[lboardOrder[0]])
            else:
                lboard_name = args[1][2:]
                view_leaderboard(lboard_name, lboards_dict[lboard_name])

        # print all leaderboards, and specify current/active leaderboard
        elif args[0] == "--list":
            print "The existing leaderboards are: " + ", ".join(str(x) for x in lboards_dict.keys())
            print "The active leaderboard is currently: '" + lboardOrder[0] + "'"

        # send user to view players function
        elif args[0] == "--players":
            view_players(players)
        
        # send user to change leaderboard function
        elif args[0] == "--change":
            change_lboard(lboards_dict, args)

        # print help function
        elif args[0] == "--help":
            print_help()

        elif args[0] == "--search":
            search_terms = args[1:]
            if len(search_terms) != 0:
                if args[1].startswith("--"):
                    # search a specific leaderboard
                    search_terms = args[2:]
                    lb_name = args[1][2:]
                    search_players(lb_name, search_terms, lboards_dict[lb_name])
                else:
                    # search all leaderboards
                    for person in search_terms:
                        flag = 0
                        for board in lboards_dict:
                            if person in lboards_dict[board]:
                                flag = 1
                                search_players(board, person, lboards_dict[board])
                        if flag == 0:
                            print person + " is unranked in all leaderboards."


        else:
            "Invalid argument provided."
            exit()


if __name__ == "__main__":
    main()
