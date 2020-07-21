"""
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
"""

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index_dict = {}
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in index_dict:
                index_dict[sorted_nums[i]] = i

        return [index_dict[i] for i in nums]


if __name__ == "__main__":
    a = Solution()
    print a.smallerNumbersThanCurrent([8,1,2,2,3])
