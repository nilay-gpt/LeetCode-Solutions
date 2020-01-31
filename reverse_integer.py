"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""



class Solution():
    def rev_int(self, x):
        if x == 0:
            return 0
        # if x > 0:
        #     result = int(str(x)[::-1])
        # else:
        #     result = int('-' + str(x)[1:][::-1])
        # if(abs(result) > 2 ** 31):
        #     return 0
        # return result

        #one liner for the above solution main logic
        result = int(str(x)[::-1]) if x > 0 else int('-' + str(x)[1:][::-1])
        if(abs(result) > 2 ** 31): return 0


        return result



if __name__ == "__main__":
    obj = Solution()
    print obj.rev_int(1563847412)
