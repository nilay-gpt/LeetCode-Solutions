"""
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

https://leetcode.com/problems/consecutive-characters/
"""


class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_count, count, start, str_len = 0, 1, s[0], len(s)

        if str_len == 1: return 1

        for i in range(str_len-1):
            if s[i+1] == start:
                count, start  = count+1, s[i+1]
                if count > max_count: max_count = count
            else:
                if count > max_count: max_count = count
                count, start = 1, s[i+1]

        return max_count

if __name__ == "__main__":

    a = Solution()
    print a.maxPower("a")
