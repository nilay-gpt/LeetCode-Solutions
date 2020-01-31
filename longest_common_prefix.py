"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution():
    def common_prefix(self, input_list):
        if not input_list: return ""
        input_list = sorted(input_list)
        prefix = input_list[0]
        for i in range(len(input_list) -1):
            prefix = self.common_prefix_util(prefix, input_list[i+1])
            if not prefix:
                prefix = ""
                break

        return prefix

    def common_prefix_util(self, input1, input2):
        input1_len = len(input1)
        input2_len = len(input2)
        i, j = 0, 0
        prefix = ""

        while i <= input1_len - 1 and j <= input2_len - 1:
            if input1[i] == input2[j]:
                prefix += input1[i]
                i += 1
                j += 1
            else:
                break

        return prefix



if __name__ == "__main__":
    obj = Solution()
    input_list = []
    result = obj.common_prefix(input_list)
    print result
