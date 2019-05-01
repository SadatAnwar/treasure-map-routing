from unittest import TestCase

from src.treasure_finder import TreasureFinder
from src.treasure_map import TreasureMap


class TestIntegrationTreasureFinder(TestCase):

    def test_get_shortest_path_should_return_shortest_path_for_normal_challenge(self):
        treasure_map = TreasureMap()
        treasure_map.start = 0
        treasure_map.treasure = 9
        treasure_map.roads = [(0, 1), (1, 2), (1, 3), (1, 4), (2, 5), (3, 5), (3, 7), (4, 8), (5, 6), (6, 9), (7, 8),
                              (7, 9)]
        subject = TreasureFinder(treasure_map)
        path = subject.get_shortest_path()

        self.assertEqual(path, [0, 1, 3, 7, 9])

    def test_get_treasure_avoiding_dragons_should_return_shortest_path_for_dragon_challenge(self):
        treasure_map = TreasureMap()
        treasure_map.start = 0
        treasure_map.treasure = 9
        treasure_map.roads = [(0, 1), (1, 2), (1, 3), (1, 4), (2, 5), (3, 5), (3, 7), (4, 8), (5, 6), (6, 9), (7, 8),
                              (7, 9)]
        subject = TreasureFinder(treasure_map)
        path = subject.get_treasure_avoiding_dragons([7, 8])

        self.assertEqual(path, [0, 1, 2, 5, 6, 9])

    def test_get_path_avoiding_shortest_path_roads_should_return_shortest_path_for_neighbour_challenge(self):
        treasure_map = TreasureMap()
        treasure_map.start = 0
        treasure_map.treasure = 8
        treasure_map.roads = [(0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (2, 6), (3, 7), (4, 5), (5, 8), (6, 7), (6, 8)]
        subject = TreasureFinder(treasure_map)
        path = subject.get_path_avoiding_shortest_path_roads()

        self.assertEqual(path, [0, 1, 4, 5, 8])
