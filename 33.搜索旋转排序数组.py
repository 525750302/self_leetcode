#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        mid = (left + right + 1) // 2
        while left <= right:
            mid = (left + right + 1) // 2
            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            if nums[left] <= nums[mid]:
                if nums[left] < target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <  nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        if left < len(nums) and nums[left] == target:
            return left
        if right >= 0 and nums[right] == target:
            return right
        print(left, right,mid)
        return -1
            
            
            
# @lc code=end

