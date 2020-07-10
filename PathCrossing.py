"""
Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
"""

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        diff = arr[0] - arr[1]
        for i in range(1, len(arr) -1):
            if arr[i] - arr[i+1] != diff: return False
        return True



if __name__ == "__main__":
    a = Solution()
    print a.canMakeArithmeticProgression([11,3,5,7,9,10])
