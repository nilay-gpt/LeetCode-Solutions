"""
Binary search: divide and then decide to get the value in left or right side.

                     Best    Average       Worst        (Worst Space Complexity)
Binary Search        O(1)      O(nlogn)    O(log n)        O(1)


"""

class BinarySearch(object):
    def main_search(self, traget, item_list):

        floor_index = -1
        ceil_index = len(item_list)

        while floor_index + 1 < ceil_index:

            distance = ceil_index - floor_index
            half_distance = distance / 2
            guess_index = floor_index + half_distance

            guess_value = item_list[guess_index]

            if guess_value == traget:
                return True

            if guess_value > traget:
                ceil_index = guess_index
            else:
                floor_index = guess_index
        return False



if __name__ == "__main__":
    obj = BinarySearch()
    print obj.main_search(7, [1,2,3,4,5,6,7,8,9,10])
