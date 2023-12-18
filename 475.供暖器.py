#
# @lc app=leetcode.cn id=475 lang=python
#
# [475] 供暖器
#

# @lc code=start
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        res = 0
        for house in houses:
            l, r = 0, len(heaters) - 1
            while l <= r:
                mid = (l + r) // 2
                if heaters[mid] > house:
                    r = mid - 1
                else:
                    l = mid + 1
            print(l,r)
            if l == 0:
                res = max(res, heaters[l] - house)
            elif r == len(heaters) - 1:
                res = max(res, house - heaters[r])
            else:
                res = max(res, min(house - heaters[l - 1], heaters[r + 1] - house))
        return res
# @lc code=end

