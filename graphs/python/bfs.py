from Graph import Graph
from Graph import build_test_graph
from Vertex import Vertex

def bfs(vertex, value):
	"""
	Input: starting Vertex, value to find
	Output: return closest Vertex that contains value

	Graph is a digraph. So it has cycles. Values can repeat.
	"""
	neighbors = []
	visited = set() #all unique elements
	neighbors.append(vertex)
	while len(neighbors) > 0:
		vertex = neighbors.pop(0)
		if vertex.value == value:
			return vertex
		for neighbor in vertex.neighbors:
			if neighbor not in visited:
				neighbors.append(neighbor)
				visited.add(neighbor)
	return None




def test_bfs():
	graph = build_test_graph()
	graph.pretty_print()

	vertices = graph.vertices
	v1 = vertices[0] #A
	v2 = vertices[1] #B
	v3 = vertices[2] #C
	v4 = vertices[3] #D
	v5 = vertices[4] #E

	assert bfs(v1,"B") == v2
	assert bfs(v1,"C") == v3
	assert bfs(v1,"D") == v4
	assert bfs(v1,"E") == v5

	assert bfs(v2,"A") == v1
	assert bfs(v3,"A") == v1
	assert bfs(v3,"E") == v5

if __name__ == "__main__":
	test_bfs()

