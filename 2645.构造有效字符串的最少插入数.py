#
# @lc app=leetcode.cn id=2645 lang=python
#
# [2645] 构造有效字符串的最少插入数
#

# @lc code=start
class Solution(object):
    def addMinimum(self, word):
        """
        :type word: str
        :rtype: int
        """
        target = ["a","b","c"]
        state = 0
        res = 0
        for c in word:
            if c == target[state]:
                state += 1
                state = state % 3
            else:
                while target[state] != c:
                    state += 1
                    state = state % 3
                    res += 1
                state += 1
                state = state % 3
        if state == 1:
            res += 2
        if state == 2:
            res += 1
        return res

# @lc code=end

