"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

https://leetcode.com/problems/course-schedule/
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        BFS approch
        > create graph for indexes and dependency list with.
        > create inorder for indexes saying the inorder degree.
        > create stack with all the indegree as 0 in it
        > mentain count and add +1 while adding anything to stack
        """
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        count = 0
        
        # fill graph list to have dependency list
        for i, j in prerequisites:
            graph[i].append(j)
            indegree[j] += 1
        
        # have stack for all the indegree 0
        stack = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                count += 1
                stack.append(i)
                
        while stack:
            i = stack.popleft()
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    stack.append(j)
                    count += 1

        return count == numCourses
