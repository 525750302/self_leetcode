#
# @lc app=leetcode.cn id=2012 lang=python
#
# [2012] 数组美丽值求和
#

# @lc code=start
class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = [0] * len(nums)
        max_val = [0] * len(nums)
        max_data = 0
        min_data = 1000000
        min_val = [1000000] * len(nums)
        for i in range(1, len(nums)):
            max_data = max(max_data, nums[i-1])
            max_val[i] = max_data
        for i in range(len(nums) - 1, 0, -1):
            min_data = min(min_data, nums[i])
            min_val[i-1] = min_data
        res = 0
        for i in range(len(nums) - 2, 0, -1):
            if max_val[i] < nums[i] and min_val[i] > nums[i]:
                res += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                res += 1
            
        
        return res
# @lc code=end

