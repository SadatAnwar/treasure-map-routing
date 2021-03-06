from typing import List, Optional

from src.graph import Graph
from src.treasure_map import TreasureMap


class TreasureFinder:
    _graph: Graph
    _start: int
    _destination: int

    def __init__(self, treasure_map: TreasureMap):
        self._start = treasure_map.start
        self._destination = treasure_map.treasure
        self._graph = Graph()
        for road in treasure_map.roads:
            self._graph.add_edge(road[0], road[1])

    def get_shortest_path(self) -> List[int]:
        """
        For task 1, we simply return the shortest path from the start till the destination

        :return: return the shortest path if it exists
        """
        return self._graph.find_shortest_path(self._start, self._destination)

    def get_treasure_avoiding_dragons(self, dragons: List[int]) -> List[int]:
        """
        For task 2 we need to avoid dragons, but only when they sneeze i.e nodes 3, 6, 9 ... of the path should not
        have a dragon on them. We can circle around 2 previous nodes in order to cross the dragon after its finished
        sneezing. see method _circle_before_dragon
        :param dragons:
        :return:
        """
        all_paths: List[List[int]] = self._graph.find_all_paths(self._start, self._destination)

        if len(all_paths) == 0:
            return []

        possible_paths = []

        for path in all_paths:
            if self._will_burn(path, dragons):
                p = self._circle_before_dragon(path, dragons)
                if p is not None:
                    possible_paths.append(p)
            else:
                possible_paths.append(path)

        return self._get_shortest_list(possible_paths)

    def get_path_avoiding_shortest_path_roads(self) -> List[int]:
        """
        For task 3 we need to avoid the rodes taken by the annoying neighbour. We also know that the neighbour will be
        taking the shortest path. So, we can simply find the shortest path, and then remove all the rodes it contains from
        the original graph. We then find the shortest path again, and if there exists a path, this is the solution.

        :return: Returns a path that avoids the rodes on the shortest path of the original map
        """
        shortest_path = self.get_shortest_path()
        road_segments = self._get_road_segments(shortest_path)
        self._graph.remove_roads(road_segments)

        return self._graph.find_shortest_path(self._start, self._destination)

    @staticmethod
    def _get_shortest_list(possible_paths: List[List[int]]) -> List[int]:
        if len(possible_paths) > 0:
            possible_paths.sort(key=lambda l: len(l))
            return possible_paths[0]
        else:
            return []

    @staticmethod
    def _will_burn(path, dragons):
        return any([path[i] in dragons for i in range(3, len(path), 3)])

    @staticmethod
    def _get_road_segments(path: List[int]):
        return [(path[i - 1], path[i]) for i in range(1, len(path))]

    def _circle_before_dragon(self, path, dragons) -> Optional[List[int]]:
        """
        Helper method to circle around a dragon node.

        Since dragons sneeze every 15 mins, and it takes 5 mins to travel between nodes, we could cycle between 2 nodes
        to avoid a dragons sneeze.
        eg:
           you have nodes 0 -> 1 -> 2 -> 3 -> 4
           dragons = [3]
           start = 0
           treasure = 4

           shortestPath = [0,1,2,3,4]
           however dragon node is hit at minute 15, so this path would not work, we could do 0->1->2->1->2->3->4
           this would make us cross the dragon node at 25 (10 mins later) and avoid a sneeze

        :param path:
        :return:
        """

        check = 3
        while check < len(path):
            if path[check] in dragons:
                # If there are 3 consecutive dragons, then there is no possible solution
                if path[check + 1] in dragons and path[check + 2] in dragons:
                    path.clear()
                    return None
                path.insert(check, path[check - 2])
                path.insert(check + 1, path[check - 1])
            check += 3

        if self._will_burn(path, dragons):
            self._circle_before_dragon(path, dragons)
        else:
            return path
