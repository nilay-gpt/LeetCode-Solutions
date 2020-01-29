"""
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count_dict = {}
        output_list = []
        for i in chars:
            if i in count_dict:
                count_dict[i] = count_dict[i] + 1
            else:
                count_dict[i] = 1
        print count_dict
        chars=[]
        for key, value in count_dict.items():
            chars.append(key)
            if value > 1 and value <= 9:
                chars.append(value)
            elif value >=10:
                chars.extend(list(str(value)))
        return len(chars)
        print chars


if __name__ == "__main__":
    a = Solution()
    a.compress(["a","b","b","b","b","b","b","b","b","b"])
