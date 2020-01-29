# Using a Python dictionary to act as an adjacency list
"""
          A
         / \
        B   C
              \
       / \     F
      D   E -----
"""


graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visitied_node = []

def dfs(visitied_node, graph, node):
	if node not in visitied_node:
		print node
		visitied_node.append(node)
		
		for child in graph[node]:
			dfs(visitied_node, graph, child)

dfs(visitied_node, graph, "A")
