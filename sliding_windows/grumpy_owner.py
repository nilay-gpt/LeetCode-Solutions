"""
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

https://leetcode.com/problems/grumpy-bookstore-owner/
"""


class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        # when the owner is not grumpy, keeping the total sum to tally in window approach
        total_sum = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                total_sum += customers[i]

        max_total = total_sum

        for left in range(len(customers)- X+1):
            delta_total = 0
            for j in range(left, X):
                if grumpy[j] == 1:
                    delta_total += customers[j]
            if total_sum + delta_total > max_total:
                max_total = total_sum + delta_total
            X += 1

        return max_total


        
        # m = s = tmp = 0
        # for i in range(len(customers)):
        #     if not grumpy[i]: 
        #         s += customers[i]                # sum of satisfied customers
        #         customers[i] = 0 
        #     else: tmp += customers[i]            # sum of grumpy customers 
        #     if i>=X: tmp -= customers[i-X]       # remove the leftmost element to keep the sliding window with # of X
        #     m = max(m, tmp)                      # max # of satisfied grumpy customers with a secret technique
        # return s+m




if __name__ == "__main__":
    a = Solution()
    print a.maxSatisfied([1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3)




