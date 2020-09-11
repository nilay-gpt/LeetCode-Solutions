"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
"""

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # taking N+1 because there are no people as '0' and in the 2nd loop
        # the for will start from 1st position.
        # main point to remember: All people in town must trust the judge.
        # means in the graph all people must be pointing to judge.

        people_list = [0] * (N+1)        
        for i, j in trust:
            people_list[i] -= 1
            people_list[j] += 1
        
        for i in range(1, N+1):
            if people_list[i] == N-1:
                return i
        return -1
    
