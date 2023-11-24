#
# @lc app=leetcode.cn id=858 lang=python
#
# [858] 镜面反射
#

# @lc code=start
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def lcm(x, y):
            from math import gcd
            return x * y // gcd(x, y)
        
        lcm_pq = lcm(p, q)
        if (lcm_pq//p) % 2 == 0:
            return 0
        if (lcm_pq//q) % 2 == 0:
            return 2
        else:
            return 1

# @lc code=end

