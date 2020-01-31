"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
"""

class Solution(object):
    def remove_elements(self, nums, val):
        length = len(nums)
        i = 0
        while length > i:
            if nums[i] == val:
                del nums[i]
                length -= 1
            else:
                i += 1    

        return len(nums)


if __name__ == "__main__":
    obj = Solution()
    print obj.remove_elements([0,1,2,2,3,0,4,2], 2)
