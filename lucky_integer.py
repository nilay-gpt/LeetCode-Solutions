"""
"""
import collections


class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count_dict = dict(collections.Counter(arr))
        output = -1
        for key, value in count_dict.items():
            if key == value and value > output:
                output = value
        return output

if __name__ == "__main__":
    
    a = Solution()
    print a.findLucky([2,3,4])
