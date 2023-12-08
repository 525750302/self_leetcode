#
# @lc app=leetcode.cn id=2008 lang=python
#
# [2008] 出租车的最大盈利
#

# @lc code=start
class Solution(object):
    def maxTaxiEarnings(self, n, rides):
        """
        :type n: int
        :type rides: List[List[int]]
        :rtype: int
        """
        rides.sort(key=lambda x: x[1])
        for i in range(len(rides)):
            rides[i][2] = rides[i][1] - rides[i][0] + rides[i][2]
        dp = [0] *( n + 1)
        user = 0
        print(rides)
        for i in range(n + 1):
            dp[i] = dp[i-1]
            while user < len(rides) and  rides[user][1] == i:
                dp[i] = max(dp[i], rides[user][2] + dp[rides[user][0]],dp[i-1])
                user += 1

        return max(dp)

# @lc code=end

