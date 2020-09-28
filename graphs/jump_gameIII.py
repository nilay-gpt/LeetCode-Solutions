"""
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3

https://leetcode.com/problems/jump-game-iii/
"""

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        return self.dfs(arr, start, 0)
    
    
    def dfs(self, arr, start, count):
        if start < 0 or start >= len(arr) or count >= len(arr): return False
        if arr[start] == 0: return True

        return self.dfs(arr, start-arr[start], count+1) or self.dfs(arr, start+arr[start], count+1)
