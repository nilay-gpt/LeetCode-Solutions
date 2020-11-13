"""

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""

https://leetcode.com/problems/reorganize-string/
"""


import collections, heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        """"
        algo: Have the counter for all the chars in S
              Have a max heap to keep the most frequent on the top.
              once this is done then use the top and the second top and
                append in the output.
        """
        count_dict = collections.Counter(S)
        heap = []
        out = ""
        
        for char, freq in count_dict.items():
            heapq.heappush(heap, (-freq, char))
            
        while heap:
            #heapq pop syntax to remember here
            first_freq, first_char = heapq.heappop(heap)
            out += first_char
            
            if not heap:
                if first_freq < -1:
                    return ""
                #break from the while.
                break

            second_freq, second_char = heapq.heappop(heap)
            out += second_char
            
            if first_freq < -1:
                heapq.heappush(heap, (first_freq + 1, first_char))
                
            if second_freq < -1:
                heapq.heappush(heap, (second_freq + 1, second_char))
                
        return out
