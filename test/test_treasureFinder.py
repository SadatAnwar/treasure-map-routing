from unittest import TestCase, mock
from unittest.mock import call

from src.graph import Graph
from src.treasure_finder import TreasureFinder
from src.treasure_map import TreasureMap


class TestTreasureFinder(TestCase):
    treasure_map = TreasureMap()
    treasure_map.start = 0
    treasure_map.treasure = 5

    @mock.patch.object(Graph, 'find_shortest_path')
    def test_get_shortest_path_should_call_graph_find_shortest_path(self, mock_find_shortest_path):
        subject = TreasureFinder(self.treasure_map)
        subject.get_shortest_path()

        mock_find_shortest_path.assert_called_with(0, 5)

    @mock.patch.object(Graph, 'find_all_paths')
    def test_get_treasure_avoiding_dragons_should_get_all_paths(self, mock_find_all_paths):
        subject = TreasureFinder(self.treasure_map)
        subject.get_treasure_avoiding_dragons([])

        mock_find_all_paths.assert_called_with(0, 5)

    @mock.patch.object(Graph, 'find_all_paths')
    def test_get_treasure_avoiding_dragons_should_return_valid_path(self, mock_find_all_paths):
        mock_find_all_paths.return_value = [[1, 2, 3, 4, 5, 6], [1, 2, 6]]

        subject = TreasureFinder(self.treasure_map)
        path = subject.get_treasure_avoiding_dragons([3, 4, 5])

        self.assertEqual(path, [1,2,6])

    @mock.patch.object(Graph, 'remove_roads')
    @mock.patch.object(Graph, 'find_shortest_path')
    def test_get_path_avoiding_shortest_path_roads_should_get_shortest_path_and_remove_those_roads(self,mock_shortest_path,mock_remove_roads):
        mock_shortest_path.return_value = [0, 1, 2, 3]
        subject = TreasureFinder(self.treasure_map)
        subject.get_path_avoiding_shortest_path_roads()

        calls = [call(0, 5), call(0, 5)]  # find_shortest_path should be called twice

        mock_shortest_path.assert_has_calls(calls)
        mock_remove_roads.assert_called_with([(0, 1), (1, 2), (2, 3)])
