#
# @lc app=leetcode.cn id=2681 lang=python
#
# [2681] 英雄的力量
#

# @lc code=start
class Solution(object):
    def sumOfPower(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        nums.sort()
        ans = s = 0
        for x in nums:  # x 作为最大值
            ans = (ans + x * x * (x + s)) % MOD
            s = (s * 2 + x) % MOD  # 递推计算下一个 s
        return ans
# @lc code=end

