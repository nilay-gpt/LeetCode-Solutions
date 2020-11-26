"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # WILL NOT work [0,0,1,1], 0
        # for i in range(len(numbers)):
        #     if target - numbers[i] in numbers:
        #         return [i+1, numbers.index(target - numbers[i])+1]
        
        # two pointers
        l, r = 0, len(numbers)-1
        
        while l < r:
            if numbers[l] + numbers[r] == target: return [l+1, r+1]
            if  numbers[l] + numbers[r] > target: r -= 1
            else: l += 1
