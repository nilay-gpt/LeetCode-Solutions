"""
Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.

https://leetcode.com/problems/longest-repeating-character-replacement/
"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i = max_len = max_count = 0
        window = [0] * 26

        for j in range(len(s)):
            window[ord(s[j]) - ord('A')] += 1 #only capital letters are allowed.
            max_count = max(max_count, window[ord(s[j]) - ord('A')])

            while j - i + 1 - max_count > k:
                window[ord(s[i]) - ord('A')] -= 1
                i += 1

            max_len = max(max_count, j - i + 1)

        return max_len   


if __name__ == "__main__":
    a = Solution()
    print a.characterReplacement(s = "ABAB", k = 2)
