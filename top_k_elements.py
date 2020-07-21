"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""
import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        sorted_dict = collections.Counter(nums)
        print sorted_dict
        sorted_nums =  sorted(sorted_dict, key=sorted_dict.get, reverse=True)
        return sorted_nums[:k]


if __name__ == "__main__":
	a = Solution()
	print a.topKFrequent([1,1,1,2,2,3], k = 2)
