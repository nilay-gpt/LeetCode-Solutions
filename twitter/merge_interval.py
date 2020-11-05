"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

https://leetcode.com/problems/merge-intervals/
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda a:a[0])
        
        output = []
        
        for i in intervals:
            if not output or output[-1][1] < i[0]:
                output.append(i)
            else:
                output[-1][1] = max(output[-1][1], i[1])
        return output
