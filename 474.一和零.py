#
# @lc app=leetcode.cn id=474 lang=python
#
# [474] 一和零
#

# @lc code=start
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for i in range(m + 1)]
        num_1 = []
        num_0 = []
        for i in strs:
            num_0.append(0)
            num_1.append(0)
            for j in range(len(i)):
                if i[j] == "1":
                    num_1[-1] += 1
                elif i[j] == "0":
                    num_0[-1] += 1
        
        for i in range(len(strs)):
            numOf1 = num_1[i]
            numOf0 = num_0[i]
            for j in range(m,numOf0-1,-1):
                for k in range(n,numOf1-1,-1):
                    dp[j][k] = max(dp[j][k],dp[j-numOf0][k-numOf1] + 1)

        
        return dp[m][n]


# @lc code=end

