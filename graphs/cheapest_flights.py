"""
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:

https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(dict)
        for s,d,i in flights:
            graph[s][d] = i

        heap = [(0, src, K+1)]

        while heap:
            p, s, k = heapq.heappop(heap)

            if s == dst:
                return p

            if k > 0:
                for j in graph[s]:
                    heapq.heappush(heap, (p+graph[s][j], j, k-1))


        return -1
