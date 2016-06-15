from abc import abstractmethod

class TraversalStrategy:
	
	@abstractmethod
	def traverse_from_source(self, source, adjacency_list):
		...
