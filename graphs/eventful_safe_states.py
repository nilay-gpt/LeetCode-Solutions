"""
In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.

https://leetcode.com/problems/find-eventual-safe-states/
"""

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        Just move along unvisited (-1) nodes and remark them as 0 on the queue while visiting others on the path and finish them as 1. If you meet them again on the queue while visiting (being 0) it means you completed a cycle, in other words it is not safe and return back without adding.
        """
        visited, result = [-1] * len(graph), []
        
        def explore(i):
            visited[i] = 0
            for v in graph[i]:
                if visited[v] == 0 or (visited[v]==-1 and explore(v)): return True
            visited[i] = 1
            result.append(i)
            return False
        
        for i in range(len(graph)):
            if visited[i] == -1: explore(i)

        return sorted(result)
            
