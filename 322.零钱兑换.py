#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#

# @lc code=start
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp =[9999999] * (amount+1)
        dp[0] = 0
        coins.sort()
        print(coins)
        for step in coins:
            begin = step
            while begin <= amount:
                dp[begin] = min(dp[begin],dp[begin - step] + 1)
                begin += 1
        if dp[amount] == 9999999:
            return -1
        return dp[amount]
# @lc code=end

