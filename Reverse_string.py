class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s = s[::-1]
        print s

if __name__ == "__main__":
	a=Solution()
	a.reverseString(["h","e","l","l","o"])
