#
# @lc app=leetcode.cn id=633 lang=python
#
# [633] 平方数之和
#

# @lc code=start
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 2:
            return True
        for i in range(1, int(c ** 0.5) + 1):
            a = c - i ** 2
            root = int(a ** 0.5)
            if root * root == a:
                return True
        
        return False
# @lc code=end

