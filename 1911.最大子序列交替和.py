#
# @lc app=leetcode.cn id=1911 lang=python
#
# [1911] 最大子序列交替和
#

# @lc code=start
class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive_dp = [0] * len(nums)
        passitive_dp = [0] * len(nums)
        positive_dp[0] = nums[0]
        for i in range(len(nums)):
            positive_dp[i] = max(positive_dp[i],positive_dp[i-1],passitive_dp[i - 1] + nums[i])
            passitive_dp[i] = max(passitive_dp[i],passitive_dp[i - 1],positive_dp[i - 1] - nums[i])
        return positive_dp[-1]
# @lc code=end

