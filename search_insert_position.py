"""
Given a sorted nums and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the nums.
Input: [1,3,5,6], 5
Output: 2

"""

class Solution(object):
    def search_position(self, nums, x):
        if x in nums:
            index = nums.index(x) 
        else:
            nums.append(x)
            nums.sort()
            index = nums.index(x)
        return index



if __name__ == "__main__":
    obj =Solution()
    nums = [1,5,6,7,8,9]
    x = -2

    print obj.search_position(nums, x)
