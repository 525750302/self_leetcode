#
# @lc app=leetcode.cn id=123 lang=python
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0] * 4 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        dp[0][2] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], - prices[i])
            dp[i][1] = max(dp[i - 1][0] + prices[i], dp[i - 1][1])
            dp[i][2] = max(dp[i - 1][1]- prices[i], dp[i - 1][2])
            dp[i][3] = max(dp[i - 1][2] + prices[i], dp[i - 1][3])
        #print(dp)
        return max(dp[-1])
# @lc code=end

