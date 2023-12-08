#
# @lc app=leetcode.cn id=2216 lang=python
#
# [2216] 美化数组的最少删除数
#

# @lc code=start
class Solution(object):
    def minDeletion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        check = True
        for i in range(n - 1):
            if nums[i] == nums[i + 1]  and check:
                ans += 1
            else:
                check = not check
        if (n - ans) % 2 != 0:
            ans += 1
        return ans 

# @lc code=end

