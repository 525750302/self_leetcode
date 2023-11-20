#
# @lc app=leetcode.cn id=1003 lang=python
#
# [1003] 检查替换后的词是否有效
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if self.check(s,0) == len(s):
            return True
        else:
            return False


    def check(self,s,point):
        if s[point] != "a":
            return -1
        point += 1
        if point >= len(s):
            return -1
        if s[point] == "a":
            point = self.check(s,point)
            if point == -1:
                return -1
        if point >= len(s) or s[point] != "b":
            return -1

        point += 1
        if point >= len(s):
            return -1
        if s[point] == "a":
            point = self.check(s,point)
            if point == -1:
                return -1
        if point >= len(s) or s[point] != "c":
            return -1
        point += 1
        if point < len(s) and s[point] == "a":
            point = self.check(s,point)
            if point == -1:
                return -1
        return point
# @lc code=end

