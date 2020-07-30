"""
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 
Example 1:
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

https://leetcode.com/problems/max-consecutive-ones-iii/
"""

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        left = right = 0

        for right in range(len(A)):
            if A[right] == 0:
                K -= 1
            if K < 0:
                if A[left] == 0:
                    K += 1

                left += 1
        return right - left +1

if __name__ == "__main__":
    a = Solution()
    print a.longestOnes( A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3)
