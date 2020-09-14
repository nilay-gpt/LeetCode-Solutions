"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:

Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
 
Example 2:

Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.



https://leetcode.com/problems/friend-circles/submissions/
Exp video: https://www.youtube.com/watch?v=63env_9M03U
"""

class UnionFind(object):
    def __init__(self):
        self.parent = {}

    def make_set(self, x):
        self.parent[x] = x

    def find(self, x):
        if x not in self.parent:
            self.make_set(x)
            return x

        elif self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_set = self.find(x)
        y_set = self.find(y)

        if x_set != y_set:
            self.parent[x_set] = y_set
            return False
        return True

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        self.m_len = len(M)
        self.circles = self.m_len

        if not M: return 0
        uf = UnionFind()

        for row in range(self.m_len):
            row_len = len(M[row])
            for col in range(row_len):
                if row != col and M[row][col]: #as the person is always friends with himself
                    if not uf.union(row, col):
                         self.circles -= 1
        return self.circles
