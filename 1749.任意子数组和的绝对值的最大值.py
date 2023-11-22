#
# @lc app=leetcode.cn id=1749 lang=python
#
# [1749] 任意子数组和的绝对值的最大值
#

# @lc code=start
class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = [0]
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            pre.append(sum)
        print(pre)
        return max(pre) - min(pre)

# @lc code=end

