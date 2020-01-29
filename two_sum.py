"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        key_dict = {}
        for index, num in enumerate(nums):
            other = target - num
            if other in key_dict:
                return [key_dict[other], index]
            else:
                key_dict[num] = index
                
        return []

if __name__ == '__main__':
    a = Solution()
    a.twoSum([3,2,4], 6)
