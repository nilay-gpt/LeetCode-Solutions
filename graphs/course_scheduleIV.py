"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have direct prerequisites, for example, to take course 0 you have first to take course 1, which is expressed as a pair: [1,0]

Given the total number of courses n, a list of direct prerequisite pairs and a list of queries pairs.

You should answer for each queries[i] whether the course queries[i][0] is a prerequisite of the course queries[i][1] or not.

Return a list of boolean, the answers to the given queries.

Please note that if course a is a prerequisite of course b and course b is a prerequisite of course c, then, course a is a prerequisite of course c.

Input: n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[1,3],[3,0]]
Output: [true,false,true,false]

https://leetcode.com/problems/course-schedule-iv/
"""

from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # DFS approch + LRU caching
        # LRU: It saves the repeatation and returns if pre calculated
        graph = defaultdict(list)
        
        for i, j in prerequisites:
            graph[i].append(j)
            
        @lru_cache(None)
        def is_reachable(source, dest):
            if source == dest: return True
            
            for neigh in graph[source]:
                if is_reachable(neigh, dest): return True
            return False
        
        result = []
        for s, d in queries:
            result.append(is_reachable(s, d))

        return result
                                
