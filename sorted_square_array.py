"""
You have a sorted array as input and have to return a sorted squared array of input.

Solutions:
> Brute force:   Square all the given element in the list and sort the o/p. But complexity will be O(n log n)
> Best solution: Initialize one output list with all 0's of the length of input list. Then have 2 pointers(i(start) and j(end) on the given list.
                 Comapre the square of i and j and then keep in the postion from backwords in the o/p list.
                 Complexity will be O(n)

i/p = [-7, -3, -1, 4, 8, 12] => [1, 9, 16, 49, 64, 144]
"""

class SortedSquareList(object):
    def __init__(self, input_list):
        self.list = input_list

    def sorted_squared_list(self):
        output_list = [0] * len(self.list)
        i, j, replacing_index = 0, len(self.list) - 1, len(self.list) - 1

        for element in self.list:
            square_of_i, square_of_j = self.list[i] * self.list[i], self.list[j] * self.list[j]
            if square_of_i > square_of_j: output_list[replacing_index], i = square_of_i, i+1
            else: output_list[replacing_index], j = square_of_j, j-1

            replacing_index -= 1
        return output_list


if __name__ == "__main__":
    input_list = [-7, -3, -1, 4, 8, 12]
    obj = SortedSquareList(input_list)
    print obj.sorted_squared_list()
