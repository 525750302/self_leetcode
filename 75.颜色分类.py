#
# @lc app=leetcode.cn id=75 lang=python
#
# [75] 颜色分类
#

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        num_of_color = [0,0,0]
        result = []
        for i in range(len(nums)):
            num_of_color[nums[i]] += 1
        k = 0
        for i in range(3):
            for j in range(num_of_color[i]):
                nums[k] = i
                k += 1

# @lc code=end

