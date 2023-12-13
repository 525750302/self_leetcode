#
# @lc app=leetcode.cn id=2697 lang=python
#
# [2697] 字典序最小回文串
#

# @lc code=start
class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        s = list(s)
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                s[i]= s[n - 1 - i] = min(s[n - 1 - i], s[i])
        return ''.join(s)
# @lc code=end

