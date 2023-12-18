#
# @lc app=leetcode.cn id=983 lang=python
#
# [983] 最低票价
#

# @lc code=start
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        days.sort()
        dp = [0] * (days[-1] + 1)
        for i in range(days[-1] + 1):
            if i in days:
                dp[i] = min(dp[max(0, i - 1)] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
            else:
                dp[i] = dp[i - 1]
        return dp[-1]

# @lc code=end

