import copy

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return ((nums[-1] - 1) * (nums[-2] - 1))


if __name__ == "__main__":
	a = Solution()
	print a.maxProduct([3,7])
