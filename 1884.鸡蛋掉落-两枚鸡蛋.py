#
# @lc app=leetcode.cn id=1884 lang=python
#
# [1884] 鸡蛋掉落-两枚鸡蛋
#

# @lc code=start
class Solution(object):
    def twoEggDrop(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 1
        for i in range(1, n + 1):
            sum += i
            if sum > n:
                return i
# @lc code=end

