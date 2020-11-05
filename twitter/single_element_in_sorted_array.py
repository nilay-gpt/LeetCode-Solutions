"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

https://leetcode.com/problems/single-element-in-a-sorted-array/
"""


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # following solution is O(n) and asked is O(log)
        # for i in range(0, len(nums)-2, 2):
        #     if nums[i] != nums[i+1]:
        #         return nums[i]
        # return nums[-1]
        
        #Binary search for O(log n)
        
        low, high = 0, len(nums) -1
        
        while low < high:
            mid = 2 * ((low + high) // 4)
            if nums[mid] == nums[mid+1]:
                low = mid + 2
            else:
                high = mid
        
        return nums[low]
    
