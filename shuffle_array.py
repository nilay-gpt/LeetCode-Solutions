"""
"""

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        output_array = []
        for i in range(len(nums)/2):
            output_array.append(nums[i])
            output_array.append(nums[i+n])
        return output_array


if __name__ == "__main__":
    a = Solution()
    print a.shuffle(nums = [1,2,3,4,4,3,2,1], n = 4)
