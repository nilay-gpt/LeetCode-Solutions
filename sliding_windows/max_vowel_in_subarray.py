"""
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_count, vowel_list = 0, ['a', 'e', 'i', 'o', 'u']

        # for left in range(len(s) - k+1):
        #     local_max = 0
        #     for i in range(left, k):
        #         if s[i] in vowel_list: local_max +=1
        #     if local_max > max_count: max_count = local_max
        #     k += 1
        # print count :
        # return max_count

        max_count, current_count, vowel = 0, 0, "aeiou"

        for i in range(len(s)):
            if i >= k:
                if s[i-k] in vowel:
                    current_count -=1
            if s[i] in vowel:
                current_count += 1
            max_count = max(max_count, current_count)
        return max_count

if __name__ == "__main__":
    a = Solution()
    print a.maxVowels("leeecodeeee", k = 3)
