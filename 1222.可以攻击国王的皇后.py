#
# @lc app=leetcode.cn id=1222 lang=python
#
# [1222] 可以攻击国王的皇后
#

# @lc code=start
class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(8):
            if [king[0], king[1] - i] in queens:
                res.append([king[0], king[1] - i])
                break
        for i in range(8):
            if [king[0], king[1] + i] in queens:
                res.append([king[0], king[1] + i])
                break
        for i in range(8):
            if [king[0]- i, king[1]] in queens:
                res.append([king[0]- i, king[1]])
                break
        for i in range(8):
            if [king[0]+ i, king[1]] in queens:
                res.append([king[0]+ i, king[1]])
                break
        for i in range(8):
            if [king[0]-i, king[1] - i] in queens:
                res.append([king[0]-i, king[1] - i])
                break
        for i in range(8):
            if [king[0] + i, king[1] + i] in queens:
                res.append([king[0] + i, king[1] + i])
                break
        for i in range(8):
            if [king[0]+i, king[1] - i] in queens:
                res.append([king[0]+i, king[1] - i])
                break
        for i in range(8):
            if [king[0] - i, king[1] + i] in queens:
                res.append([king[0] - i, king[1] + i])
                break
        return res

# @lc code=end

