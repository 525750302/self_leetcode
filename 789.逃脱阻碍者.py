#
# @lc app=leetcode.cn id=789 lang=python
#
# [789] 逃脱阻碍者
#

# @lc code=start
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        return all(abs(target[0] - x) + abs(target[1] - y) > abs(target[0]) + abs(target[1]) for x, y in ghosts)
# @lc code=end

