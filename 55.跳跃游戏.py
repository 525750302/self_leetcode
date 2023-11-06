#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        range = nums[0]
        if range >= len(nums)-1:
            return True
        point = 1
        while point <= range:
            if range >= len(nums)-1:
                return True
            range = max(range, point + nums[point])
            point += 1
        
        return False

# @lc code=end

