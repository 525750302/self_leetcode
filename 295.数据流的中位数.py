#
# @lc app=leetcode.cn id=295 lang=python
#
# [295] 数据流的中位数
#

# @lc code=start
from sortedcontainers import SortedList
class MedianFinder(object):

    def __init__(self):
        self.left_next = SortedList()
        self.right_next = SortedList()
        self.median = 0


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.left_next) == 0 and len(self.right_next) == 0:
            self.right_next.add(num)
            self.left_next.add(num)
            self.median = num
            return
        if self.median < num:
            self.right_next.add(num)
            self.right_next.add(num)
            a = self.right_next[0]
            self.right_next.pop(0)
            self.left_next.add(a)
        elif self.median > num:
            self.left_next.add(num)
            self.left_next.add(num)
            a = self.left_next[-1]
            self.left_next.pop(-1)
            self.right_next.add(a)
        else:
            self.right_next.add(num)
            self.left_next.add(num)

        self.median = (float(self.left_next[-1]) +float(self.right_next[0]))/2
        



    def findMedian(self):
        """
        :rtype: float
        """
        return self.median



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

