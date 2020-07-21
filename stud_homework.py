"""
Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1
Explanation: We have 3 students where:
The first student started doing homework at time 1 and finished at time 3 and wasn't doing anything at time 4.
The second student started doing homework at time 2 and finished at time 2 and also wasn't doing anything at time 4.
The third student started doing homework at time 3 and 
"""

class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        count = 0 
        for i in range(len(startTime)):
            if endTime[i] >= queryTime and startTime[i] <= queryTime: count += 1

        return count


if __name__ == "__main__":
    a = Solution()
    print a.busyStudent(startTime = [4], endTime = [4], queryTime = 5)
