#
# @lc app=leetcode.cn id=901 lang=python
#
# [901] 股票价格跨度
#

# @lc code=start
class StockSpanner(object):

    def __init__(self):
        self.stack = [(10**9, 0)]
        self.day = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.day += 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        span = 1 if not self.stack else self.day - self.stack[-1][1]
        self.stack.append((price, self.day))
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

