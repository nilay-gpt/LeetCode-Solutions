class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        target.sort()
        arr.sort()
        if target==arr: return True
        else: return False
        

if __name__ == "__main__":
    a = Solution()
    print a.canBeEqual([1,2,3,4], [2,4,1,3])

# [1,2,3,4], [2,4,1,3]
# ([7], [7])
