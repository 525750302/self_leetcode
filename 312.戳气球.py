#
# @lc app=leetcode.cn id=312 lang=python
#
# [312] 戳气球
#

# @lc code=start
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0] * (len(nums)+2) for i in range(len(nums)+2)]
        nums.append(1)
        nums.insert(0,1)
        for time in range(2,len(nums)):
            for i in range(0,len(nums) - time):
                for j in range(i+1,i + time):
                    coin = nums[i] * nums[j] *nums[i+time]
                    dp[i][i+time] = max(dp[i][i+time],dp[i][j] + dp[j][i+time] + coin) 
        return dp[0][len(nums)-1]

# @lc code=end

