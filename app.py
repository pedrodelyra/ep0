from graph import Graph

if __name__ == '__main__':
	brasilia = Graph()

	brasilia.add_bidirectional_edge("fga", "darcy", 30)
	brasilia.add_bidirectional_edge("fga", "plano piloto", 45)
	brasilia.add_bidirectional_edge("fga", "iesb", 28)

	brasilia.add_bidirectional_edge("plano piloto", "guara", 22)
	brasilia.add_bidirectional_edge("fga", "guara", 150)

	brasilia.choose_traversal_strategy("FLOYD_WARSHALL")
	distance_from_fga = brasilia.traverse_from_source("fga")

	for node in distance_from_fga.keys():
		print("distance from fga to " + node + " is " + str(distance_from_fga[node]))

	print("")
	
	brasilia.choose_traversal_strategy("BELLMAN_FORD")
	distance_from_fga = brasilia.traverse_from_source("fga")

	for node in distance_from_fga.keys():
		print("distance from fga to " + node + " is " + str(distance_from_fga[node]))
