"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
"""
import collections


class Solution(object):
    def countCharacters(self, words, chars):
        count_list = [dict(collections.Counter(i)) for i in words]
        chars_count = dict(collections.Counter(chars))
        total_count = 0
        
        for i in range(len(count_list)):
            flag = True
            for key, value in count_list[i].items():

                if value > chars_count.get(key, 0):
                    flag = False
                    break
            if flag: total_count += len(words[i])
        return total_count

if __name__ == "__main__":
    a = Solution()
    print a.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr")
