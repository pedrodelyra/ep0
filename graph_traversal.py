from abc import abstractmethod
from collections import defaultdict
from queue import *

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

        for node in nodes:
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

class BellmanFord(TraversalStrategy):
    def __init__(self):
        self.INFINITY = 1 << 60

    def traverse_from_source(self, source, adjacency_list):
        distance = dict()
        nodes = []
        for node in adjacency_list.keys():
            nodes.append(node)

        for neighbour, neighbour_distance in adjacency_list[source]:
            distance[neighbour] = neighbour_distance
        distance[source] = 0

        list_length = len(adjacency_list)
        for iteration in range(0, list_length - 1):
            for node in nodes:
                for neighbour, neighbour_distance in adjacency_list[node]:
                    distance[neighbour] = min(distance[neighbour], distance[node] + neighbour_distance)

        return distance

class Dijkstra(TraversalStrategy):
	def __init__(self):
		self.INFINITY = 1 << 60

	def traverse_from_source(self, source, adjacency_list):
		distance = dict()
		nodes = []
		for node in adjacency_list.keys():
			nodes.append(node)
			distance[node] = self.INFINITY

		distance[source] = 0
		pq = PriorityQueue()
		pq.put((distance[source], source))
		while not pq.empty():
			current_state = pq.get()
			current_distance = current_state[0]
			current_node = current_state[1]

			if current_distance > distance[current_node]:
				continue

			for neighbour, neighbour_distance in adjacency_list[current_node]:
				if distance[neighbour] > distance[current_node] + neighbour_distance:
					distance[neighbour] = distance[current_node] + neighbour_distance
					pq.put((distance[neighbour], neighbour))

		return distance

class TraversalFactory():
    def build(traversal_strategy):
        if traversal_strategy == 'FLOYD_WARSHALL':
            return FloydWarshall()
        elif traversal_strategy == 'BELLMAN_FORD':
            return BellmanFord()
        elif traversal_strategy == 'DIJKSTRA':
            return Dijkstra()
