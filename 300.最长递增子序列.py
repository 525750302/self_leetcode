#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_length = [1]*len(nums)
        dp_max = nums
        for i in range(len(nums)):
            last = -1
            for j in range(i,-1,-1):
                if dp_max[j] >= nums[i]:
                    continue
                if dp_length[j] + 1 > dp_length[i]:
                    dp_length[i] = dp_length[j] + 1
        result = max(dp_length)
        return result
# @lc code=end

