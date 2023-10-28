#
# @lc app=leetcode.cn id=365 lang=python
#
# [365] 水壶问题
#

# @lc code=start
class Solution(object):
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        """
        :type jug1Capacity: int
        :type jug2Capacity: int
        :type targetCapacity: int
        :rtype: bool
        """
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        elif jug1Capacity + jug2Capacity == targetCapacity:
            return True
        
        bigger = max(jug1Capacity, jug2Capacity)
        smaller = min(jug1Capacity, jug2Capacity)
        sum = bigger + smaller
        while sum != 0:
            while sum > smaller:
                sum = sum - smaller
                if sum == targetCapacity:
                    return True
            sum += bigger
            if sum == targetCapacity:
                return True
            if sum == bigger + smaller:
                return False
        return False

        # @lc code=end

