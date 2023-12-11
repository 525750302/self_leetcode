#
# @lc app=leetcode.cn id=1648 lang=python
#
# [1648] 销售价值减少的颜色球
#

# @lc code=start
class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        res = 0
        max_val = 10**9 + 7
        if len(inventory) == 1:
            return ((orders * (inventory[0] * 2 - orders + 1)) // 2) % max_val
        inventory.append(0)
        inventory.sort()
        now = inventory.pop(-1)
        count = 1
        while orders > 0:
            target = inventory.pop(-1)
            #print((now - target) * count < orders, orders, (now - target) * count)
            if (now - target) * count < orders:
                res += (target + now + 1) * count *(now - target) // 2
                res = res % max_val
                orders -= (now - target) * count
                count += 1
                now = target
            else:
                target = now - orders // count
                res += (target + now + 1) * count *(orders // count) // 2
                res = res % max_val
                if orders % count != 0:
                    res += (orders % count) * (target)
                    res = res % max_val
                orders = 0
            #print(now,target, res, orders, orders // count)
            
        return res

            
# @lc code=end

