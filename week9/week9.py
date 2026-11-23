from networkx import Graph

# Create a graph object
graph = Graph()

# Add the 4 islands (nodes), colours as per the above diagram
graph.add_node('Blue')
graph.add_node('Green')

# Add the 7 bridges (edges), colours as per the above diagram
graph.add_edge('Blue','Green')	# e.g. this is a bridge from the Blue to Green island
graph.add_edge('Green','Blue')

# Print a report about the graph that you have just made
print(f"We have {len(list(graph.edges()))} bridges between {len(list(graph.nodes()))} islands.")