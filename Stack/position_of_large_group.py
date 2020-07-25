"""
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.

 

Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.

https://leetcode.com/problems/positions-of-large-groups/
"""


class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        groupped_list, count, output = self.group_by(S), 0, []

        for i in range(len(groupped_list)):
            if len(groupped_list[i]) >= 3:
                temp_list = [count, count + len(groupped_list[i]) - 1]
                output.append(temp_list)

            count = count + len(groupped_list[i])
        return output
        
    def group_by(self, S):
        groupped_list, temp_list, break_flag = [], [], False
        if len(S) == 1:
            return [S[-1]]

        for i in range(0, len(S)-1):
            if not break_flag and S[i] == S[i+1]: temp_list, break_flag = [S[i]], True

            elif break_flag and S[i] == S[i+1]: temp_list.append(S[i])

            elif S[i] != S[i+1] and len(temp_list) !=0 or break_flag:
                temp_list.append(S[i])
                groupped_list.append(temp_list)
                break_flag, temp_list = True, []

            else:
                temp_list, break_flag = [S[i]], True
                groupped_list.append(temp_list)
                temp_list = []

        # to process the last list.
        if temp_list:
            if temp_list[-1] == S[-1]:
                temp_list.append(S[-1])
                groupped_list.append(temp_list)
            else:
                groupped_list.append(temp_list)
                groupped_list.append([S[-1]])
        elif S[-1] != S[-2]:
            groupped_list.append([S[-1]])

        return groupped_list



if __name__ == "__main__":
    a = Solution()
    print a.largeGroupPositions("abbxxxxzzy")
