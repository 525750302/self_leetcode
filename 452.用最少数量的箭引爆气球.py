#
# @lc app=leetcode.cn id=452 lang=python
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:(x[1]))
        right = points[0][1]
        left = 0
        result = 0
        while left < len(points):
            while left < len(points) and points[left][0] <= right:
                left += 1
            if left < len(points):
                right = points[left][1]
            result += 1
        return result

# @lc code=end

