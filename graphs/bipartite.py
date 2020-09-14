"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.


https://leetcode.com/problems/is-graph-bipartite/
"""

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # Approch: color every alternate node with either blue(0) or red(1)
        # if there is consistency and no two same color are in seq the true else false
        colored_map = {} 
        # BFS approch
        for node in range(len(graph)):
            if node not in colored_map:
                stack = collections.deque([node])
                colored_map[node] = 0
                while stack:
                    current = stack.popleft()
                    for neighbour in graph[current]:
                        if neighbour not in colored_map:
                            colored_map[neighbour] = 1 - colored_map[current]
                            stack.append(neighbour)
                        elif colored_map[neighbour] == colored_map[current]:
                            return False
        return True 
