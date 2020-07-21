"""
Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.

 

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
"""

class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort(), salary.pop(0), salary.pop(-1)
        return float(sum(salary))/len(salary)



if __name__ == "__main__":
	a = Solution()
	print a.average([48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000])
