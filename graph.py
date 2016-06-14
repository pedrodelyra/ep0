from collections import defaultdict

class Graph:

	def __init__(self):
		self.adjacency_list = defaultdict(list)
		self.visiteds = 0

	def add_edge(self, node, neighbour, cost):
		self.adjacency_list[node].append((neighbour, cost))	

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
