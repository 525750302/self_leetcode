#
# @lc app=leetcode.cn id=1921 lang=python
#
# [1921] 消灭怪物的最大数量
#

# @lc code=start
class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        time = [0] * len(dist)
        for i in range(len(dist)):
            time[i] = dist[i]//speed[i] + (dist[i] % speed[i] != 0)
        time.sort()
        for i in range(len(time)):
            if time[i] <= i:
                return i
        return len(time)
        
# @lc code=end

