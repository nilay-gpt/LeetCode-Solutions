"""
Given a string, sort it in decreasing order based on the frequency of characters.

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

https://leetcode.com/problems/sort-characters-by-frequency/
"""
import collections


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        output_string = ""
        s_dict = collections.Counter(s)
        sorted_dict =  sorted(s_dict, key=s_dict.get, reverse=True)
        for i in sorted_dict:
            output_string += i * s_dict[i]
        return output_string
        
        


if __name__ == "__main__":
    a = Solution()
    print a.frequencySort("tree")
