from collections import defaultdict
from graph_traversal import TraversalFactory

class Graph:

	def __init__(self):
		self.adjacency_list = defaultdict(list)
		self.traversal_strategy = None
		self.visiteds = 0

	def choose_traversal_strategy(self, traversal_strategy):
		self.traversal_strategy = TraversalFactory.build(traversal_strategy)

	def traverse_from_source(self, source):
		return self.traversal_strategy.traverse_from_source(source, self.adjacency_list)

	def add_unidirectional_edge(self, node, neighbour, distance):
		self.adjacency_list[node].append((neighbour, distance))

	def add_bidirectional_edge(self, node, neighbour, distance):
		self.adjacency_list[node].append((neighbour, distance))
		self.adjacency_list[neighbour].append((node, distance))

	def __str__(self):
		result = ""
		for node in self.adjacency_list.keys():
			result += str(node) + " = ["
			for neighbour in self.adjacency_list[node]:
				result += str(neighbour)
			result += "]\n"
		return result

	def __iter__(self):
		return self

	def __next__(self):
		if self.visiteds < len(self.adjacency_list):
			count = 0
			for node in self.adjacency_list.keys():
				if count == self.visiteds:
					self.visiteds += 1
					return node
				count += 1
		else:
			self.visiteds = 0
			raise StopIteration
