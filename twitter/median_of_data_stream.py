"""

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2

"""


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # have min heap and max heap here
        #exp:https://www.youtube.com/watch?v=EcNbRjEcb14&ab_channel=happygirlzthappygirlzt
        self.max = []
        self.min = []
        

    def addNum(self, num: int) -> None:
        heappush(self.max, -num)
        heappush(self.min, -self.max[0])
        heappop(self.max)

        if len(self.max) < len(self.min):
            heappush(self.max, -self.min[0])
            heappop(self.min)
        # print(self.max)
        # print(self.min)
        

    def findMedian(self) -> float:
        if len(self.min) < len(self.max):
            return -self.max[0]
        else:
            return (self.min[0] - self.max[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
