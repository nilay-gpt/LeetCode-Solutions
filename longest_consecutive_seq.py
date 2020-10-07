"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

https://leetcode.com/problems/longest-consecutive-sequence/
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums = set(nums)
        max_len = 0

        while nums:
            num = nums.pop()
            l1=0
            l2=0
            i = num + 1
            while i in nums:
                nums.remove(i)
                i += 1
                l1 += 1

            i = num -1
            while i in nums:
                nums.remove(i)
                i -= 1
                l2 += 1

            max_len = max(max_len, l1+l2+1)
        return max_len
