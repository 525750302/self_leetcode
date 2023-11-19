#
# @lc app=leetcode.cn id=689 lang=python
#
# [689] 三个无重叠子数组的最大和
#

# @lc code=start
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dp = [0]*(len(nums)-k+1)
        ans = [0,k,2*k]
        max_location = 0
        for i in range(k):
            dp[0] += nums[i]
        for i in range(1,len(nums)-k+1):
            dp[i] = dp[i-1] - nums[i-1] + nums[i+k - 1]
        sum1, maxSum1, maxSum1Idx = 0, dp[0], 0
        sum2, maxSum12, maxSum12Idx = 0, dp[k] + dp[0], (0,k)
        sum3, maxTotal = 0, dp[k] + dp[0] + dp[k*2]

        for i in range(k * 2, len(nums) - k + 1):
            sum1 = dp[i - k * 2]
            sum2 = dp[i - k]
            sum3 = dp[i]

            if sum1 > maxSum1:
                maxSum1 = sum1
                maxSum1Idx = i - k * 2
            if maxSum1 + sum2 > maxSum12:
                maxSum12 = maxSum1 + sum2
                maxSum12Idx = (maxSum1Idx, i - k)
            if maxSum12 + sum3 > maxTotal:
                maxTotal = maxSum12 + sum3
                ans = [*maxSum12Idx, i]

        return ans

                    

# @lc code=end

