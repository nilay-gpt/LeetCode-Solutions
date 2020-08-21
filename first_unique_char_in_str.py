"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

https://leetcode.com/problems/first-unique-character-in-a-string/
"""

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # for i in range(len(s)):
        #     if s.count(s[i]) == 1:
        #         return i
        # return -1
        map_value = Counter(s)
        for i in range(len(s)):
            if map_value[s[i]] == 1:
                return i
        return -1
