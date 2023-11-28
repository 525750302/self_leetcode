#
# @lc app=leetcode.cn id=1670 lang=python
#
# [1670] 设计前中后队列
#

# @lc code=start
class FrontMiddleBackQueue(object):

    def __init__(self):
        self.stack = []

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.insert(0, val)
    


    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.insert(len(self.stack)// 2, val)


    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)


    def popFront(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1
        return self.stack.pop(0)


    def popMiddle(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1
        return self.stack.pop(len(self.stack)// 2 - (len(self.stack) % 2 == 0))


    def popBack(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return -1
        return self.stack.pop(-1)



# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
# @lc code=end

