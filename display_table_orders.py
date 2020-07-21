"""
Input: orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 

https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/
"""

class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        items = set()
        table = set()
        order_dict = {}
        for i in orders:
            items.add(i[2])
            table.add(int(i[1]))
            if i[1] not in order_dict:
                order_dict[i[1]] = dict()

            if i[2] not in  order_dict[i[1]]:
                order_dict[i[1]][i[2]] = 1
            else:
                order_dict[i[1]][i[2]] += 1

        sorted_items = sorted(items)
        sorted_table = sorted(table, key=int)

        output = [[i for i in sorted_items]]
        output[0].insert(0, 'Table')

        for number in sorted_table:
            table_list = [str(order_dict[str(number)].get(i, 0)) for i in sorted_items]
            table_list.insert(0, str(number))
            output.append(table_list)

        return output



if __name__ == "__main__":
    a = Solution()
    print a.displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]])
