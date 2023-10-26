#
# @lc app=leetcode.cn id=115 lang=python
#
# [115] 不同的子序列
#

# @lc code=start
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        max_num = 10**9 + 7
        dp = [[0] * (len(s) + 1) for i in range(len(t) + 1)]
        for i in range(len(s) + 1):
            dp[0][i] = 1
        for i in range(1,len(t) + 1):
            for j in range(i,len(s) + 1):
                if t[i-1] == s[j-1]:
                    dp[i][j] += dp[i-1][j-1]
                dp[i][j] += dp[i][j-1]
        return dp[len(t)][len(s)]
# @lc code=end

