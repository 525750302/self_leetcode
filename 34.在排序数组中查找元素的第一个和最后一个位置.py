#
# @lc app=leetcode.cn id=34 lang=python
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1,-1]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right -1) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        first = left
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        last = right
        if first > last:
            return [-1, -1]
        else:
            return [first, last]

# @lc code=end

