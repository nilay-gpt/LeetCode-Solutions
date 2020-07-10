"""
We are given a list nums of integers representing a list compressed with run-length encoding.
Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
"""
class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output_list = []
        for i in range(1 ,len(nums), 2):
            output_list += [nums[i]] * nums[i- 1]
        return output_list


if __name__ == "__main__":
    a = Solution()
    print a.decompressRLElist([1,1,2,3])
