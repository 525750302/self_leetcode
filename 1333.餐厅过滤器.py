#
# @lc app=leetcode.cn id=1333 lang=python
#
# [1333] 餐厅过滤器
#

# @lc code=start
class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        res  = []
        for i in restaurants:
            if veganFriendly == 1 and i[2] == 1:
                res.append(i)
            elif veganFriendly == 0:
                res.append(i)
        res.sort(key=lambda x: x[3])
        for i in range(len(res)):
            if res[i][3] > maxPrice:
                res = res[:i]
                break
        res.sort(key=lambda x: x[4])
        for i in range(len(res)):
            if res[i][4] > maxDistance:
                res = res[:i]
                break
        res.sort(key=lambda x: (-x[1], -x[0]))
        return [i[0] for i in res]



# @lc code=end

