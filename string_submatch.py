"""Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

https://leetcode.com/problems/string-matching-in-an-array/
"""

class Solution(object):
    def stringMatching(self, words):
        join_words = ' '.join(words)
        return set([word for word in words if join_words.count(word)> 1])

if __name__ == "__main__":
    a = Solution()
    print a.stringMatching(["ypmfx","jjuexkmb","ypmfxj"])
