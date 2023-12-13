#
# @lc app=leetcode.cn id=1654 lang=python
#
# [1654] 到家的最少跳跃次数
#

# @lc code=start
class Solution(object):
    def minimumJumps(self, forbidden, a, b, x):
        """
        :type forbidden: List[int]
        :type a: int
        :type b: int
        :type x: int
        :rtype: int
        """
        forbidden = set(forbidden)
        q = [(0, 0, 0)]
        visited = set()
        while q:
            cur, step, flag = q.pop(0)
            if cur == x:
                return step
            if cur in forbidden:
                continue
            if cur + a not in visited and cur + a <= 2000 + b * 2:
                q.append((cur + a, step + 1, 0))
                visited.add(cur + a)
            if cur - b not in visited and cur - b >= 0 and flag == 0:
                q.append((cur - b, step + 1, 1))
        return -1
# @lc code=end

