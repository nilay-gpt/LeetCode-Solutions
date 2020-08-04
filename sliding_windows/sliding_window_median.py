"""
Input:
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
Therefore, return the median sliding window as [1,-1,-1,3,5,6]. for k = 3
for k = 2, [2.00000,1.00000,-2.00000,1.00000,4.00000,4.50000,6.50000]
for k = 4, [0.00000,1.00000,1.00000,4.00000,5.50000]

https://leetcode.com/problems/sliding-window-median/
"""


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        sorted_list = []
        output = []

        for i in range(len(nums)):
            sorted_list.append(nums[i])
            sorted_list.sort()
            if len(sorted_list) == k:
                if k%2==0: output.append(float((sorted_list[k/2-1] + sorted_list[k/2]))/2)
                else: output.append(float(sorted_list[k/2]))
                
                sorted_list.remove(nums[i-(k-1)])
        
        return output


if __name__ == "__main__":
    a = Solution()
    print a.medianSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
