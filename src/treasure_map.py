from enum import Enum


class TreasureMap:
    mapType = 0
    start = -1
    treasure = -1
    roads = []
    dragons = []
    expectedRoutes = []


class MapType(Enum):
    NORMAL = 1
    DRAGON = 2
    RIVALRY = 3
