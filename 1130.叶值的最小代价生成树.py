#
# @lc app=leetcode.cn id=1130 lang=python
#
# [1130] 叶值的最小代价生成树
#

# @lc code=start
class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n =len(arr)
        dp = [[999999999] * len(arr) for i in range(len(arr))]
        mval = [[0 for i in range(n)] for j in range(n)]
        for i in range(len(arr)):
            dp[i][i] = 0
            mval[i][i] = 0
        for i in range(len(arr)-1):
            dp[i][i+1] = arr[i] * arr[i + 1]
        
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                mval[i][j] = max(mval[i][j-1],arr[j])
        for k in range(2,len(arr)):
            for begin in range(len(arr)-k):
                for mid in range(begin,begin+k):
                    add_val = mval[begin][mid] * mval[mid + 1][begin + k]
                    dp[begin][begin + k] = min(dp[begin][mid] + dp[mid + 1][begin + k] + add_val, dp[begin][begin + k])
        return dp[0][len(arr) - 1]
# @lc code=end
