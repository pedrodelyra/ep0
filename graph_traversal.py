from abc import abstractmethod
from collections import defaultdict

class TraversalStrategy:
    
    @abstractmethod
    def traverse_from_source(self, source, adjacency_list):
        ...

class FloydWarshall(TraversalStrategy):
    def __init__(self):
        self.INFINITY = 1 << 60

    def traverse_from_source(self, source, adjacency_list):
        nodes = []
        for node in adjacency_list.keys():
            nodes.append(node)
        
        distance = defaultdict(dict)
        
        for source_node in nodes:
            for destination_node in nodes:
                distance[source_node][destination_node] = self.INFINITY

        for node in adjacency_list.keys():
            for neighbour, neighbour_distance in adjacency_list[node]:
                distance[node][neighbour] = neighbour_distance
            distance[node][node] = 0
            
        list_length = len(adjacency_list)
        for current_node_position in range(0, list_length):
            current_node = nodes[current_node_position]
            for first_node in nodes:
                for second_node in nodes:
                    distance[first_node][second_node] = min(distance[first_node][second_node],
                                                       distance[first_node][current_node] + distance[current_node][second_node])


        return distance[source]

class TraversalFactory():
    def build(traversal_strategy):
        if traversal_strategy == 'FLOYD_WARSHALL':
            return FloydWarshall()