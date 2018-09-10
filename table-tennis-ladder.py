import random
import sys
# leaderboard ladder
ladder = []
#players = ['q','w','e','r','t','y','u','i','o','p','a','s','d','g','h','j','k','l','z','x','c','v','b','n','m']
players = []

#def create_players():
    #for i in range(1,2000):
        #players.append(str(i))

def get_players(filename):
    players_file = open(filename,"w+")
    players = list(players_file.read())
    players_file.close()
    return players

def write_players(filename):
    players_file = open(filename,"w+")
    players_file.write(str(players))
    players_file.close()

def get_ladder(filename):
    ladder_file = open(filename,"w+")
    ladder = list(ladder_file.read())
    ladder_file.close()
    return ladder

def write_ladder(filename):
    ladder_file = open(filename,"w+")
    ladder_file.write(str(ladder))
    ladder_file.close()

def match_played(winner,loser):
    if winner not in ladder:
        if loser not in ladder:
            ladder.append(winner)
            ladder.append(loser)
        else:
            loser_index = ladder.index(loser)
            ladder.insert(loser_index,winner)
    else:
        if loser not in ladder:
            ladder.append(loser)
        else:
            if ladder.index(winner) > ladder.index(loser):
                loser_index = ladder.index(loser)
                winner_index = ladder.index(winner)
                del ladder[winner_index]
                ladder.insert(loser_index,winner)

def tournament():
    count = 0
    for x in range(1,1000000):
        p1 = random.choice(players)
        p2 = random.choice(players)
        if p1 != p2:
            match_played(p1,p2)
            count += 1
    print count


def main():
    players = get_players("players.txt")
    ladder = get_ladder("ladder.txt")
    print "-- Menu --"
    print "1) Add players"
    print "2) Record a match"
    print "3) View Leaderboard"
    print "4) Exit"
    print ""
    user_choice = str(raw_input("Please select an option: "))

    if user_choice == "1" or user_choice == "1)":
        while True:
            player_name = str(raw_input("Please enter a name: "))
            players.append(player_name)
            user_fin = str(raw_input("Add more players? y/n: "))
            if user_fin == "n":
                write_players("players.txt")
                main()
    elif user_choice == "2" or user_choice == "2)":
        while True:
            winner = str(raw_input("Please enter name of winner: "))
            if winner not in players:
                print "Name not recognised. Please try again."
            else:
                break
        while True:
            loser = str(raw_input("Please enter name of loser: "))
            if loser not in players:
                print "Name not recognised. Please try again."
            else:
                break
        match_played(winner, loser)
    elif user_choice == "3" or user_choice == "3)":
        # to do: write a function to print the ladder nicely
        print ladder
    elif user_choice == "4" or user_choice == "4)":
        exit
    else:
        print "Invalid menu option selected."


main()
#create_players()
# tournament() 
#print(players)
#print(ladder)