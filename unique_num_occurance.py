"""
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
https://leetcode.com/problems/unique-number-of-occurrences/
"""

class Solution(object):
    def uniqueOccurrences(self, arr):
        arr_set = set(arr)
        count = list()
        for i in arr_set:
            count.append(arr.count(i))

        if len(count) == len(set(count)):
            return True
        else:
            return False


if __name__ == "__main__":
    a = Solution()
    print a.uniqueOccurrences([1,2])
