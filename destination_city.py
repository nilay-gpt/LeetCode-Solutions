"""
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
"""

class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        end_points, start_points = set(), set()

        for i in paths:
            start_points.add(i[0])
            end_points.add(i[1])

        return end_points.difference(start_points).pop()
        



if __name__ == "__main__":
    a = Solution()
    print a.destCity( [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]])
