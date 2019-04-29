from collections import defaultdict
from typing import List, Dict, Tuple


class Graph:
    _vertices: Dict[int, List[int]] = {}

    def __init__(self):
        self._vertices = defaultdict(list)

    def add_edge(self, node1: int, node2: int):
        # Add the forward and reverse direction
        self._vertices[node1].append(node2)
        self._vertices[node2].append(node1)

    def remove_node(self, node: int):
        connections = self._vertices[node]
        self._vertices[node] = []
        for n in connections:
            self._vertices[n].remove(node)

    def remove_roads(self, roads: List[Tuple[int, int]]):
        for road in roads:
            self.remove_road(road)

    def remove_road(self, road: Tuple[int, int]):
        self._vertices[road[0]].remove(road[1])
        self._vertices[road[1]].remove(road[0])

    def find_path(self, source: int, treasure_node: int) -> List[int]:
        """
        Finds a path from the source till the treasure_node if one exists.
        This method uses the Breadth First Search (BFS) to find the treasure_node, while keeping track of the path taken

        The path returned is the shortest path from source to destination

        :param source: The starting node
        :param treasure_node: The destination node
        :return: The path from start to destination
        """

        # Mark all the vertices as not visited
        visited: List[bool] = [False for _ in self._vertices.keys()]
        # a list to maintain the predecessor of each node. Initialize by -1 (i.e no predecessor)
        predecessor: List[int] = [-1 for _ in self._vertices.keys()]

        # a list of nodes that need to be inspected
        nodes_to_follow: List[int] = []

        # Add the source node to the list. (We start looking from here)
        nodes_to_follow.append(source)
        # Also mark it as visited
        visited[source] = True

        path_exists = False

        while nodes_to_follow and not path_exists:
            # Get the next node
            node = nodes_to_follow.pop(0)

            # Get all nodes that are accessible from node
            # if the reachable_node has not been visited, then mark it
            # visited and enqueue it (to be followed in a later iteration)
            for reachable_nodes in self._vertices[node]:
                if not visited[reachable_nodes]:
                    nodes_to_follow.append(reachable_nodes)
                    visited[reachable_nodes] = True
                    predecessor[reachable_nodes] = node

                    # Stop when we hit the treasure node
                    if reachable_nodes == treasure_node:
                        path_exists = True
                        break

        if path_exists:
            return self._make_path(treasure_node, predecessor)
        else:
            return []

    def find_all_paths(self, source: int, destination: int) -> List[List[int]]:
        """
        Find all the path that exist from source to destination.

        This uses the Depth First Search (DFS) to find all paths that exist in the graph.

        :param source: Starting node
        :param destination: Destination node

        :return: List of all possible paths that exist
        """
        result_paths: List[List[int]] = []
        visited: List[bool] = [False for _ in self._vertices.keys()]

        self._depth_traversal(source, destination, [], visited, result_paths)

        return result_paths

    def _depth_traversal(self, start: int, destination: int, path: List[int], visited: List[bool], result_paths: List[List[int]]):
        visited[start] = True
        path.append(start)
        if start == destination:
            result_paths.append([p for p in path])
            visited[destination] = False
            return
        for node in self._vertices[start]:
            if not visited[node]:
                self._depth_traversal(node, destination, path, visited, result_paths)
                path.remove(node)

        visited[start] = False

    @staticmethod
    def _make_path(destination: int, predecessor: List[int]):
        """
        This method returns the path from start to destination in an array.
        It constructs the path by starting at the destination and then back tracking till the end, thereby reaching
        the start.

        :param destination: The destination node
        :param predecessor: The array containing the predecessor of each node. p[i] contains the node before node i
        :return: the path from start till the destination node
        """

        # add destination to the path
        path = [destination]
        while predecessor[destination] != -1:
            path.append(predecessor[destination])
            destination = predecessor[destination]

        # Since the path is constructed from destination to source, we need to return its inverse
        return path[::-1]
