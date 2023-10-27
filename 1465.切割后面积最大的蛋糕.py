#
# @lc app=leetcode.cn id=1465 lang=python
#
# [1465] 切割后面积最大的蛋糕
#

# @lc code=start
class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        MAX_NUM = 10**9 + 7

        distance_h = []
        distance_W = []
        horizontalCuts.sort()
        horizontalCuts.insert(0,0)
        horizontalCuts.append(h)
        verticalCuts.sort()
        verticalCuts.insert(0,0)
        verticalCuts.append(w)
        h_Num = len(horizontalCuts)
        w_Num = len(verticalCuts)
        max_w = 0
        max_h = 0
        for i in range(h_Num-1):
            max_h = max((h-horizontalCuts[i]) - (h-horizontalCuts[i+1]),max_h)
        for i in range(w_Num-1):
            max_w = max((w-verticalCuts[i]) - (w-verticalCuts[i+1]),max_w)
        
        return (max_h * max_w) % MAX_NUM

# @lc code=end

