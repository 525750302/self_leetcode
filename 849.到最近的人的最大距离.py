#
# @lc app=leetcode.cn id=849 lang=python
#
# [849] 到最近的人的最大距离
#

# @lc code=start
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_dis = 0
        last = -1
        first = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                if max_dis < i - last:
                    max_dis = i - last
                    if last == -1:
                        first = i
                last = i
        
        res = max(first, max_dis // 2)
        if seats[-1] == 0:
            res = max(res, len(seats) - 1 - last)
        return res
# @lc code=end

