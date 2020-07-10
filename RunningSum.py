"""
Given an array nums. We define a running sum of an array.

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""

class Solution(object):
    def running_sum(self, nums):
        global_sum = 0
        output = list()
        for i in nums:
            global_sum += i
            output.append(global_sum)
        return output

if __name__ == "__main__":
    a = Solution()
    answer = a.running_sum([1, 1,1, 1, 1])
    print answer
