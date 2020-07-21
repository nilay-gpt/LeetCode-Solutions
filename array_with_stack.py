"""
Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.

Return the operations to build the target array.

You are guaranteed that the answer is unique.

 

Example 1:

Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation: 
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]

https://leetcode.com/problems/build-an-array-with-stack-operations/
"""

class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        output = []
        compare_list = []
        for i in range(1, n+1):
            if i in target:
                compare_list.append(i)
                output.append('Push')
            else:
                output.append('Push')
                output.append('Pop')
            if compare_list == target:
                break
        return output


if __name__ == "__main__":
    a = Solution()
    print a.buildArray(target = [2,3,4], n = 4)
