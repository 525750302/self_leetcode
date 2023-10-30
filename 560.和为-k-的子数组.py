#
# @lc app=leetcode.cn id=560 lang=python
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = len(nums)
        pre = {}
        count = 0
        result = 0
        for i in range(len(nums)):
            pre[count] = 1 if pre.get(count) == None else pre[count] + 1
            count += nums[i]
            if count - k in pre.keys():
                result += pre[count - k]

        return result


# @lc code=end

