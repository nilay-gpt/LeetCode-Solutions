"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3

https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
"""

import collections

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        count_dict = dict(collections.Counter(A))
        for key, value in count_dict.items():
            if value == len(A)/2:
                return key
        return None
        

if __name__ == "__main__":
    call = Solution()
    print call.repeatedNTimes([2,1,2,5,3,2])
