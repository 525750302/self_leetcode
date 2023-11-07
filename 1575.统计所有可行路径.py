#
# @lc app=leetcode.cn id=1575 lang=python
#
# [1575] 统计所有可行路径
#

# @lc code=start
MAX_VAL = 10**9 + 7
class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        n = len(locations)
        dp = [[0] * (fuel + 1) for _ in range(n)]
        dp[start][0] = 1
        for i in range(fuel + 1):
            for j in range(n):
                for k in range(n):
                    if j == k:
                        continue
                    if dp[j][i] and abs(locations[j] - locations[k]) + i <= fuel:
                        dp[k][i + abs(locations[j] - locations[k])] += dp[j][i]
        return sum(dp[finish]) % MAX_VAL

# @lc code=end

