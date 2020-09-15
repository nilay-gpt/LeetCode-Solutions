"""
Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

 

Example 1:

Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.
Example 2:

Input: ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
Example 3:

Input: ["a==b","b==c","a==c"]
Output: true
Example 4:

Input: ["a==b","b!=c","c==a"]
Output: false
Example 5:

Input: ["c==c","b==d","x!=z"]
Output: true

https://leetcode.com/problems/satisfiability-of-equality-equations/
"""
class UnionFind(object):
    def __init__(self):
        self.parent = {}

    def check_if_already_present(self, x):
        return x in self.parent

    def make_parent(self, x):
        self.parent[x] = x
        return x

    def find(self, x):
        if x not in self.parent:
            self.make_parent(x)
            return x

        elif self.parent[x] == x: return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root: self.parent[x_root] = y_root

        return True


class Solution:
    def equationsPossible(self, equations):
        un_equal_eq = []
        uf = UnionFind()

        for equation in equations:
            if  equation[1] == "=": uf.union(equation[0], equation[-1])
            else: un_equal_eq.append(equation)

        for equation in un_equal_eq:
            if uf.find(equation[0]) == uf.find(equation[-1]): return False

        return True
