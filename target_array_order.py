"""
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]

https://leetcode.com/problems/create-target-array-in-the-given-order/
"""


class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        for i in range(len(index)):
            target[index[i]:index[i]] = [nums[i]]

        return target
        
if __name__ == "__main__":
    a = Solution()
    print a.createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1])
