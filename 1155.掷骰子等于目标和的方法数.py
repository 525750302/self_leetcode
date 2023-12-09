#
# @lc app=leetcode.cn id=1155 lang=python
#
# [1155] 掷骰子等于目标和的方法数
#

# @lc code=start
class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        max_val = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1,n + 1):
            for j in range(1,min(target + 1, i * k + 1)):
                for x  in range(1, k + 1):
                    if j - x >= 0:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - x]) % max_val
        
        return dp[n][target]

# @lc code=end

