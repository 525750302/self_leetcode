#
# @lc app=leetcode.cn id=2706 lang=python
#
# [2706] 购买两块巧克力
#

# @lc code=start
class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        if prices[0] + prices[1] <= money:
            return money - prices[0] - prices[1]
        else:
            return money
# @lc code=end

