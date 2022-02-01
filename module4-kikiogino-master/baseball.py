#open filw
import re 
import math

import sys, os

if len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} filename")

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")
import re 
stats_regex = re.compile(r"(?P<rePlayer>\w* \w*) batted (?P<reBats>\d+) times with (?P<reHits>\d+) hits and (?P<reRuns>\d+) runs")


# def playerAvg ():
#     batter = re.match().group
#     batsTotal = re.match().group
#     hits = re.match().group
#     runs = re.match().group


#create a dictionary where the key is the player
#corresponding value is an object

        

#dictionary where key=player, value=statsobject
#iterate through textfile and keep adding to dictionary
player_dict = {}

#create object then add to dictionary, use dict.update()

#stats object containing amt for each player
class PlayerStats:
    # player = ""
    batsTotal = 0
    hitsTotal = 0
    
    #constructor
    def __init__(self, batsTotal, hitsTotal): 
        # self.player = player
        self.batsTotal = batsTotal
        self.hitsTotal = hitsTotal

    def average(self):
        return int(self.hitsTotal)/int(self.batsTotal)
        

    
#stats.batsTotal will have bats total for that person in the dict

# stats_regex = re.compile(r"(\w* \w*) batted (\d+) times with (\d+) hits and \d+ runs")


with open(filename) as f:
    for line in f:
       
        match = re.match(stats_regex,line)
        if match is not None:
            bats = int(match.group('reBats'))
            hits = int(match.group('reHits'))
            
            #check to see if player group exists
            #if exists, update class variables for player
            if match.group('rePlayer') in player_dict: 
                # print(match.group(rePlayer))

                player_dict[match.group('rePlayer')].batsTotal += bats
                player_dict[match.group('rePlayer')].hitsTotal += hits

            #if dne, create new key 
            else: 
                playername = match.group('rePlayer')
                
                newplayer = PlayerStats(bats, hits)
                player_dict[playername]= newplayer
                #if exists, add to group 
                #else: create new player class 
                        #new player key in dictionary
sorted_dict = {}
for key in player_dict:
    # print (key + ': ' + str(player_dict[key].average()))
    sorted_dict[key] = player_dict[key].average()
#sort method stackOverflow
sorted_dict = sorted(sorted_dict, key=sorted_dict.get, reverse=True)

for key in sorted_dict:
    print(key + ': ' + str("%.3f" % round(player_dict[key].average(),3)) )



