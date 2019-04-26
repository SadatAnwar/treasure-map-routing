import argparse
import ast
from enum import Enum


class TreasureMap:
    mapType = 0
    start = -1
    treasure = -1
    roads = []
    dragons = []
    expectedRoutes = []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('treasure_maps', help='The input problem text file')
    args = parser.parse_args()
    treasureMaps = readTreasureMap(args.treasure_maps)
    for missionID, treasureMap in enumerate(treasureMaps):
        print("Starting mission #" + str(missionID + 1) + ":")

        if treasureMap.mapType == MapType.NORMAL:
            # [TODO] call your solution here
            actualRoute = []
        elif treasureMap.mapType == MapType.DRAGON:
            # [TODO] call your solution here
            actualRoute = []
        elif treasureMap.mapType == MapType.RIVALRY:
            # [TODO] call your solution here
            actualRoute = []

        evaluateResult(treasureMap.expectedRoutes, actualRoute)


# ----------------------------------------------------------------------------

class MapType(Enum):
    NORMAL = 1
    DRAGON = 2
    RIVALRY = 3


class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def readTreasureMap(treasure_maps):
    treasureMaps = []
    with open(treasure_maps) as f:
        line = f.readline()
        while line:
            tr = TreasureMap()

            line = f.readline()
            tr.mapType = MapType(ast.literal_eval(line))
            line = f.readline()
            tr.start = ast.literal_eval(line)
            line = f.readline()
            tr.treasure = ast.literal_eval(line)
            line = f.readline()
            tr.roads = ast.literal_eval(line)
            line = f.readline()
            if tr.mapType == MapType.DRAGON:
                tr.dragons = ast.literal_eval(line)
                line = f.readline()
            tr.expectedRoutes = ast.literal_eval(line)
            line = f.readline()

            treasureMaps.append(tr)
    return treasureMaps


def evaluateResult(expectedRoutes, actualRoute):
    for expectedRoute in expectedRoutes:
        if (expectedRoute == actualRoute):
            if (len(actualRoute) == 0):
                print(bcolors.OKGREEN + "   You correctly found out that there is no route.")
            else:
                print(bcolors.OKGREEN + "   You found the treasure!")
                print("   The route takes", len(actualRoute) * 5, "minutes")
            print("  ", actualRoute, bcolors.ENDC)
            return
    print(bcolors.FAIL + "   Your route and the expected route differ:")
    print("\n   Expected Route:")
    print("  ", expectedRoutes)
    print("\n   Actual Route:")
    print("  ", actualRoute, bcolors.ENDC)
    print("--------------------")


if __name__ == "__main__":
    main()
