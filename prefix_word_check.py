"""
Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4
Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.
https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
"""

class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        split = sentence.split()
        for i in range(len(split)):
        	# if len(split[i]) >= len(searchWord) and split[i].split(searchWord)[0] == '': return i+1
        	if len(split[i]) >= len(searchWord) and split[i].startswith(searchWord): return i+1
        return -1

if __name__ == "__main__":
	a = Solution()
	print a.isPrefixOfWord(" i love eating burger", "burg")
