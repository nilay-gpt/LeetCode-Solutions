"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

https://leetcode.com/problems/verifying-an-alien-dictionary/
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {i: j for j, i in enumerate(order)}

        words = [[order_dict[w] for w in word] for word in words]
        
        for i in range(len(words)-1):
            if words[i] > words[i+1]: return False

        return True
