import csv
from bs4 import  BeautifulSoup
import requests
import Webscraping

class team:
    def __init__(self, name, stats_game1, result, led=None, matchup=None):
        self.name = name
        self.statistics = statistics
        self.matchup = matchup
        self.result = result
        self.led = led

    def getname(self):
        return self.name

    def getstats(self):
        return self.statistics

    def getpos(self):
        return self.statistics[0]

    def getXG(self):
        return self.statistics[1]

    def getT(self):
        return self.statistics[2]

    def getA(self):
        return self.statistics[3]

    def getS(self):
        return self.statistics[4]

    def getSOT(self):
        return self.statistics[5]

    def getInt(self):
        return self.statistics[6]

    def getB(self):
        return self.statistics[7]

    def getPrP(self):
        return self.statistics[8]

    def getPrC(self):
        return self.statistics[9]

    def getResult(self):
        return self.result

    def getAllStats(self):
        return self.statistics

    def pair(self, other):
        self.matchup = other
        other.matchup = self

    def compare(self):
        self.led = [False for x in range(10)]
        for i in range(len(self.statistics)):
            if self.statistics[i] > self.matchup.statistics[i]:
                self.led[i] = True

    def __str__(self):
        str = (f"{self.name} faced {self.matchup.name}")
        str += (f"\nPossesion: {self.statistics[0]}")
        str += (f"\nXG: {self.statistics[1]}")
        str += (f"\nTackles: {self.statistics[2]}")
        str += (f"\nAssists: {self.statistics[3]}")
        str += (f"\nShots: {self.statistics[4]}")
        str += (f"\nShots on Target: {self.statistics[5]}")
        str += (f"\nInterceptions: {self.statistics[6]}")
        str += (f"\nBlocks: {self.statistics[7]}")
        str += (f"\nProgressive Passes: {self.statistics[8]}")
        str += (f"\nProgressive Carries: {self.statistics[9]}")
        str += (f"\nResult: {self.getResult()}")
        return str


# initializes all teams with a given statline opponent stats from a matchday
# all teams are stored in an array/list



def assignGame(filename):
    with open(filename, newline='') as file:
        read = csv.reader(file)
        next(read)
        teams = []
        for row in read:
            name = row[0]
            stats = [float(x) for x in row[1:11]]
            result = row[11]
            curTeam = team(name, stats, result)
            teams.append(curTeam)
        for i in range(0, len(teams), 2):
            teams[i].pair(teams[i + 1])
        for i in range(len(teams)):
            teams[i].compare()

    return teams


# create map of teams name to stats for a given match
# you can find a teams stats and all their data by looking up their name

def assignTeamGameMap(filename):
    teamdict = {}
    teams = assignGame(filename)
    for team in teams:
        teamdict[team.getname()] = team
        return teamdict


# matches team name with its data for a given matchday by the filename
def teamGameFinder(filename, name):
    map = assignTeamGameMap(filename)
    if name not in map:
        return "error, team could not be found on this matchday"
    else:
        return map[name]


# creates 2D array storing two matches of a round per team
def assignRound(filename1, filename2):
    assignmentG1 = assignGame(filename1)
    assignmentG2 = assignGame(filename2)
    teamsRound = []
    for i in range(len(assignmentG2)):
        teamsRound.append([assignmentG1[i], assignmentG2])
        return teamsRound

    # links team name to round data
    def assignTeamRoundMap(filename1, filename2):
        teamdict = {}
        teamsRound = assignRound(filename1, filename2)
        for team in teamsRound:
            teamdict[team[0].getname()] = team
        return teamdict


class teamDataRound:
    def __init__(self, name, filename1, filename2, perfomances=None):
        self.name = name
        assignmentG1 = assignTeamGameMap(filename1)
        assignmentG2 = assignTeamGameMap(filename2)
        self.performances = [assignmentG1[name], assignmentG2[name]]

def statsBetterGameRaw(filename):
    # amt of times a team leading in a certain stat won for a certain day of matches
    prcntoftime = [0] * 10
    teams = assignGame(filename)
    num = len(teams) // 2
    for team in teams:
        r = team.getResult()
        if (r == "W" or r == "D"):
            for i, led in enumerate(team.led):
                if led:
                    prcntoftime[i] += 1
    return prcntoftime


# compile stats teams led in a round from both games in a round as helper function

def statsBetterRoundRaw(game1, game2):
    # team stats for game 1 and game 2 are collected
    teams1 = assignGame(game1)
    teams2 = assignGame(game2)
    # number of matches per game in round is teams//2 so total per round with two  games is equal to teams
    totalMatches = len(teams1)
    # 2 arrays hold the amount of times teams won or drew leading  in certain stats
    Leading1 = statsBetterGameRaw(game1)
    Leading2 = statsBetterGameRaw(game2)
    Leading3 = []
    for i in range(len(Leading1)):
        Leading3.append(Leading1[i] + Leading2[i])
    return Leading3


# percent  of times stats led  won or drew per round
def statsBetterRound(filename1, filename2):
    teams1 = assignGame(filename1)
    num = len(teams1)
    prcnt = statsBetterRoundRaw(filename1, filename2)
    prcnt = [float((x / num)) * 100 for x in prcnt]
    return prcnt


def statsBetterGame(filename):
    # percent of times a team leading in a certain stat won for a certain day of matches
    prcntoftime = [0] * 10
    teams = assignGame(filename)
    num = len(teams) // 2
    for team in teams:
        r = team.getResult()
        if (r == "W" or r == "D"):
            for i, led in enumerate(team.led):
                if led:
                    prcntoftime[i] += 1
    prcntoftime = [float((x / num)) * 100 for x in prcntoftime]

    return prcntoftime


def printAnalysisGame(filename):
    roundname = filename[:-4]
    out = statsBetterGame(filename)

    print(f"For the set of games  in {roundname}")
    print(f"Teams leading in Possession won or drew {out[0]}% of the time")
    print(f"Teams leading in XG won or drew {out[1]}% of the time")
    print(f"Teams leading in Tackles won or drew {out[2]}% of the time")
    print(f"Teams leading in Assists won or drew {out[3]}% of the time")
    print(f"Teams leading in Shots won or drew {out[4]}% of the time")
    print(f"Teams leading in Shots on Target won or drew {out[5]}% of the time")
    print(f"Teams leading in Interceptions won or drew {out[6]}% of the time")
    print(f"Teams leading in Blocks won or drew {out[7]}% of the time")
    print(f"Teams leading in Progressive Passes won or drew {out[8]}% of the time")
    print(f"Teams leading in Progressive Carries won or drew {out[9]}% of the time")


def printAnalysisRound(filename1, filename2):
    roundname = filename1[:-6]
    print(f"For the round {roundname}")
    out = statsBetterRound(filename1, filename2)
    print(f"Teams leading in Possession won or drew {out[0]}% of the time")
    print(f"Teams leading in XG won or drew {out[1]}% of the time")
    print(f"Teams leading in Tackles won or drew {out[2]}% of the time")
    print(f"Teams leading in Assists won or drew {out[3]}% of the time")
    print(f"Teams leading in Shots won or drew {out[4]}% of the time")
    print(f"Teams leading in Shots on Target won or drew {out[5]}% of the time")
    print(f"Teams leading in Interceptions won or drew {out[6]}% of the time")
    print(f"Teams leading in Blocks won or drew {out[7]}% of the time")
    print(f"Teams leading in Progressive Passes won or drew {out[8]}% of the time")
    print(f"Teams leading in Progressive Carries won or drew {out[9]}% of the time")


statsBetterGame("QF.1.csv")
