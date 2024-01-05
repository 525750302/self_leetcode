#
# @lc app=leetcode.cn id=1599 lang=python
#
# [1599] 经营摩天轮的最大利润
#

# @lc code=start
class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        """
        :type customers: List[int]
        :type boardingCost: int
        :type runningCost: int
        :rtype: int
        """
        max_val = -1
        time = -1
        waiting = 0
        cost = 0
        for i, c in enumerate(customers):
            waiting += c
            cost += boardingCost * min(4, waiting) - runningCost
            waiting -= min(4, waiting)
            if cost > max_val:
                max_val = cost
                time = i + 1
        add_time = 0
        if waiting > 4 and 4*boardingCost - runningCost > 0:
            cost += (4 * boardingCost - runningCost) * (waiting // 4)
            add_time = waiting // 4
        if waiting % 4 > 0 and (waiting % 4)*boardingCost - runningCost > 0:
            add_time +=1 
            cost +=(waiting % 4)*boardingCost - runningCost
        if cost > max_val:
            time = len(customers) + add_time

        return time if max_val > 0 else -1

# @lc code=end

