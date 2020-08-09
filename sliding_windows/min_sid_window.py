"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
"bdab"
"ab"

https://leetcode.com/problems/minimum-window-substring/
"""
from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target_cnt = Counter(t)
        to_be_found = len(t)
        i = 0
        min_str = ""
        for j in range(len(s)):
            # if the search letter is found then decrease the target dict count.
            if target_cnt[s[j]] > 0:
                to_be_found -= 1

            # if the search letter is not found then, insert -1 with the new alphabet.
            target_cnt[s[j]] -= 1

            # this will execute for the fist time when the t is found in s completely.
            while to_be_found == 0:
                # need to set the min_str. 
                if not min_str or j - i + 1 < len(min_str):
                    min_str = s[i:j+1]

                target_cnt[s[i]] += 1

                # If all target letters have been seen and now, a target letter is seen with count > 0
                # Increase the target length to be found. This will break out of the loop
                if target_cnt[s[i]] > 0:
                    to_be_found +=1
                i += 1
        return min_str


if __name__ == "__main__":
    a = Solution()
    print a.minWindow(s = "ADOBECODEBANC", t = "ABC")
