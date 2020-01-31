"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
Input: "42"
Output: 42

Input: "   -42"
Output: -42

Input: "4193 with words"
Output: 4193

Input: "words and 987"
Output: 0

"""

class Solution(object):
    def str_to_int(self, x):
        trimed_str = x.strip()
        result = 0
        

        try:
            result = int(trimed_str)
            result = self.check_max_limit(result)
            return result
        except:
            result = ""
            for i in trimed_str:
                if i == '-' or i == "+" or i.isdigit() :
                    result += i
                else:
                    break

        if result == "-" or result == "+": return 0
        try:
            result = int(result)
        except:
            result = 0
        # result = int(result) if result else 0
        result = self.check_max_limit(result)
        return result

    def check_max_limit(self, result):
        if abs(result) > 2**31:
            max_value = 2**31
            if result < 0: 
                result = -max_value
            else: 
                result = max_value
        return result


if __name__ == "__main__":
    obj = Solution()

    result =  obj.str_to_int(" 42")
    print type(result)
    print result
