"""
https://leetcode.com/problems/daily-temperatures/
"""


class Solution:
    def dailyTemperatures(self, nums):
        """
        Runtime: 300 ms, faster than 74.12%
        Memory Usage: 16.6 MB, less than 9.45%
        """
        res = [0] * len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)                    
        return res

if __name__ == "__main__":
	a= Solution()
	print a.dailyTemperatures([75, 71, 69, 72, 76, 73])
