from traversal_strategy import TraversalStrategy

class FloydWarshall(TraversalStrategy):
	INFINITY = 1 << 60

	def traverse_from_source(self, source, adjacency_list):
		nodes = []
		for node in adjacency_list.keys():
			nodes.append(node)
		
		cost = defaultdict(dict)
		
		for source_node in nodes:
			for destination_node in nodes:
				cost[source_node][destination_node] = INFINITY

		list_length = len(adjacency_list)
		for upper_node in range(1, list_length + 1):
			for first_node in nodes:
				for second_node in nodes:
					cost[first_node][second_node] = min(cost[first_node][second_node],
													   cost[first_node][upper_node] + cost[upper_node][second_node])


		return cost[source]
