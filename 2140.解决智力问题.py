#
# @lc app=leetcode.cn id=2140 lang=python
#
# [2140] 解决智力问题
#

# @lc code=start
class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        n = len(questions)
        dp = [0] * n
        for i in range(n):
            dp[i] = questions[i][0]
        for i in range(n):
            if i > 0:
                dp[i] = max(dp[i], dp[i-1] - questions[i - 1][0] + questions[i][0])
            if i + questions[i][1] + 1 < n:
                dp[i + questions[i][1] + 1] = max(dp[i + questions[i][1] + 1], dp[i] + questions[i + questions[i][1] + 1][0])
            #print(dp)
        return max(dp)

# @lc code=end

