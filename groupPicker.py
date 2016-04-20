from random import shuffle
import sys

def read_teams():

    # list to return with team names
    teams = list()

    # read teams line by line from file
    with open('teams.txt', 'r') as f:
        lines = f.readlines()

        # remove the newline character at end of each line
        for line in lines:
            teams.append(line.rstrip('\n'))

    return teams


def get_groups(teams, n):
    
    # randomized group list to return
    final_groups = list()

    # check to see if teams can be divided equally
    if len(teams) % n != 0:
        print("Teams cannot be evenly divided")
        sys.exit()
    else:
        
        # divide list into equal parts and get groups
        for i in range(0, len(teams), n):
            group = teams[i:i+n]
            final_groups.append(group)

    return final_groups



def main():
    
    # get teams from text file, get number of groups from user, and randomize list
    teams = read_teams()
    num_groups = int(input("Enter the number teams per group: "))
    shuffle(teams)

    # get the list of final groups
    final_groups = get_groups(teams, num_groups)

    # pring the groups
    for group in final_groups:
        for i in range(len(group)):
            print("%d) %s" % (i+1, group[i]))
        print("-----------------------------")


if __name__ == '__main__':
    main()
