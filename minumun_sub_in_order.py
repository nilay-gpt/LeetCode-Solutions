"""
Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence. 

If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array. 

Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.

 

Example 1:

Input: nums = [4,3,10,9,8]
Output: [10,9] 
Explanation: The subsequences [10,9] and [10,8] are minimal such that the sum of their elements is strictly greater than the sum of elements not included, however, the subsequence [10,9] has the maximum total sum of its elements. 

Explanation: The subsequences [10,9] and [10,8] are minimal such that the sum of their elements is strictly greater than the sum of elements not included, however, the subsequence [10,9] has the maximum total sum of its elements. 

"""

class Solution(object):
    def minSubsequence(self, nums):
        nums.sort()
        nums.reverse()
        output = []
        for i in range(len(nums)):
            if sum(nums[0:i+1]) > sum(nums[i+1:]):
                output.append(nums[i])
                break
            else: output.append(nums[i])

        return output


if __name__ == "__main__":
    a = Solution()
    print a.minSubsequence([10, 2, 11])
