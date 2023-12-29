#
# @lc app=leetcode.cn id=1276 lang=python
#
# [1276] 不浪费原料的汉堡制作方案
#

# @lc code=start
class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        if tomatoSlices % 2 == 1:
            return []
        if cheeseSlices * 2 > tomatoSlices:
            return []
        if cheeseSlices * 4 < tomatoSlices:
            return []
        return [(tomatoSlices - 2 * cheeseSlices) // 2 , cheeseSlices - (tomatoSlices - 2 * cheeseSlices) // 2]
# @lc code=end

