"""
Find the 1st duplicate number in the list.
[1,2,3,4] => -1, if no duplicate.
[2,1,3,5,3,2] =>3, because 3 is repeated before 2 in the list.
Time Com[plexity is O(n)
"""


class FindDuplicate(object):
    def __init__(self, input_list):
        self.list = input_list

    def find_duplicate(self):
        unique_set = set()

        for i in self.list:
            if i in unique_set:
                return i
            else:
                unique_set.add(i)
        return -1

if __name__ == "__main__":
    input_list = [1,2,3,4,5]
    obj = FindDuplicate(input_list)
    print obj.find_duplicate()
