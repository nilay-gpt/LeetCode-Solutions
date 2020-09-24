"""
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2

https://leetcode.com/problems/network-delay-time/
"""

from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """
        use heapq in this rather than deque or list.
        heap is a tree representaion and will mentain the shortest path accordingly in ds
        """
        graph = defaultdict(dict)
        for i, j, k in times:
            graph[i][j] = k

        stack = [(0,K)]
        dist = {}
        while stack:
            time, u = heapq.heappop(stack)
            if u not in dist:
                dist[u] = time
                for i in graph[u]:
                    heapq.heappush(stack, (graph[u][i]+time, i))

        return max(dist.values()) if len(dist) == N else -1
