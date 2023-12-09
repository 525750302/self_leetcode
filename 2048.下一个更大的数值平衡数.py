#
# @lc app=leetcode.cn id=2048 lang=python
#
# [2048] 下一个更大的数值平衡数
#

# @lc code=start
class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n + 1, 7777777):
            if self.isBalance(i):
                return i
    def isBalance(self, n):
        s = self.digit_grouping(n)
        if 7 in s or 8 in s or 9 in s or 0 in s:
            return False

        stack = {}
        for i in range(len(s)):
            stack[s[i]] = stack.get(s[i], 0) + 1

        for i in stack.keys():
            if stack[i] != int(i):
                return False
        return True
    
    def digit_grouping(self, n):
        stack = []
        while n:
            stack.append(n % 10)
            n //= 10
        return stack

# @lc code=end

