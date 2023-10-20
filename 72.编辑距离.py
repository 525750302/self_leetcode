#
# @lc app=leetcode.cn id=72 lang=python
#
# [72] 编辑距离
#

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[999999]*(len(word2)+1)for i in range(len(word1)+1)]
        dp[0][0] = 0
        for i in range(0, len(word1) + 1):
            for j in range(0, len(word2) + 1):
                if j < len(word2):
                    dp[i][j+1] = min(dp[i][j+1],dp[i][j] + 1)
                if i < len(word1):
                    dp[i+1][j] = min(dp[i+1][j],dp[i][j] + 1)
                if j < len(word2) and  i < len(word1) :
                    if word1[i]!=word2[j]:
                        dp[i+1][j+1] = min(dp[i+1][j+1],dp[i][j] + 1)
                    else:
                        dp[i+1][j+1] = min(dp[i+1][j+1],dp[i][j])
        

        return dp[len(word1)][len(word2)]

# @lc code=end

