"""
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.

 

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

https://leetcode.com/problems/k-diff-pairs-in-an-array/
"""

from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # brute force timed out
        # nums = sorted(nums)
        # count = 0
        # pair_dict = set()
        # for i in range(len(nums)):
        #     i_item = nums[i]
        #     for j in range(i+1, len(nums)):
        #         j_item = nums[j]
        #         if abs(i_item - j_item) == k and (i_item, j_item) not in pair_dict:
        #             pair_dict.add((i_item, j_item))
        #             pair_dict.add((j_item, i_item))
        #             count += 1
        # return count
        

        # have dict and get the counts(useful if k=0)
        count = Counter(nums)
        output = 0
        
        for key in count:
            if k > 0 and key + k in count:
                output += 1
                
            if k ==0 and count[key] > 1:
                output += 1

        return output
