import unittest
from typing import List, Tuple

from src.graph import Graph


def make_graph(roads: List[Tuple[int, int]]):
    graph = Graph()
    for r in roads:
        graph.add_edge(r[0], r[1])

    return graph


class TestGraph(unittest.TestCase):

    def test_bfs_should_return_shortest_path(self):
        graph = make_graph([(0, 1), (1, 2), (1, 3), (2, 5), (3, 4), (4, 5)])

        self.assertEqual(graph.find_shortest_path(0, 5), [0, 1, 2, 5])

    def test_find_shortest_path_should_return_empty_path_if_no_path_exists(self):
        graph = make_graph([(0, 1), (4, 5)])

        self.assertEqual(graph.find_shortest_path(0, 5), [], 'There should be no path present')

    def test_find_all_paths_should_return_empty_path_if_no_path_exists(self):
        graph = make_graph([(0, 1), (4, 5)])

        self.assertEqual(graph.find_all_paths(0, 5), [], 'There should be no path present')

    def test_remove_roads_should_remove_roads_between_nodes(self):
        graph = make_graph([(0, 1), (1, 2), (1, 3), (2, 5), (3, 4), (4, 5)])
        graph.remove_roads([(1, 2)])

        self.assertEqual(graph.find_shortest_path(0, 5), [0, 1, 3, 4, 5])

    def test_remove_roads_should_do_nothing_if_road_not_present(self):
        graph = make_graph([(0, 1), (1, 2), (1, 3), (2, 5), (3, 4), (4, 5)])
        graph.remove_roads([(0, 5)])

        self.assertEqual(graph.find_shortest_path(0, 5), [0, 1, 2, 5])

    def test_get_all_paths_should_return_all_possible_paths(self):
        graph = make_graph([(0, 1), (1, 2), (1, 3), (2, 5), (3, 4), (4, 5)])

        self.assertEqual(graph.find_all_paths(0, 5), [[0, 1, 2, 5], [0, 1, 3, 4, 5]])


if __name__ == '__main__':
    unittest.main()
