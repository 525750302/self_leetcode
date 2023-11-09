#
# @lc app=leetcode.cn id=131 lang=python
#
# [131] 分割回文串
#

# @lc code=start
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPalindrome(s):
            return s == s[::-1]

        def backtrack(s, start, curr):
            if start == len(s):
                res.append(curr)
                return
            for i in range(start, len(s)):
                if isPalindrome(s[start:i + 1]):
                    backtrack(s, i + 1, curr + [s[start:i + 1]])

        res = []
        backtrack(s, 0, [])
        return res
# @lc code=end

