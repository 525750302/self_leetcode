#
# @lc app=leetcode.cn id=1671 lang=python
#
# [1671] 得到山形数组的最少删除次数
#

# @lc code=start
class Solution(object):
    def minimumMountainRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = self.getLISArray(nums)
        suf = self.getLISArray(nums[::-1])[::-1]
        ans = 0

        for pre_i, suf_i in zip(pre, suf):
            if pre_i > 1 and suf_i > 1:
                ans = max(ans, pre_i + suf_i - 1)
        
        return len(nums) - ans

    def getLISArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp

# @lc code=end

