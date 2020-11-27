"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

https://leetcode.com/problems/3sum/
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3: return []
        result = []
        nums.sort()
        for i in range(0, len(nums)-2):
            if i==0 or nums[i] != nums[i-1]:
                self.two_sum(nums[i], nums[i+1:len(nums)], 0-nums[i], result)
                
        return result
        
    def two_sum(self, i, num_list, summ, result):
        left, right = 0, len(num_list)-1
        while left < right:
            level_sum = num_list[left]+num_list[right]
            if level_sum < summ: left +=1
            elif level_sum > summ : right -=1
            else:
                result.append([i, num_list[left], num_list[right]])
                left +=1
                right -=1
                
                while left<right and num_list[left] == num_list[left-1]:
                    left+=1
            
 
