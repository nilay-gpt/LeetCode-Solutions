"""
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.


https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
"""

class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        # left = last_sum = right_sum = max_value = 0
        # right = k

        # for i in range(0, k+1):
        #     left = 0 - i
        #     right_sum = sum(cardPoints[0:right])
        #     if left !=0: 
        #         last_sum = sum(cardPoints[left:])

        #     max_value = max(max_value, right_sum + last_sum)

        #     right -= 1

        # return max_value

        # following approach grows like snake game. 
        total = sum(cardPoints[:k])
        max_sum = total
        for i in range(1, k+1):
            total += cardPoints[-i] - cardPoints[k-i]
            max_sum = max(max_sum, total)
        return max_sum




if __name__ == "__main__":
    a = Solution()
    print a.maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3)

