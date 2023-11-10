#
# @lc app=leetcode.cn id=2300 lang=python
#
# [2300] 咒语和药水的成功对数
#

# @lc code=start
class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        res = []
        for spell in spells:
            target = success // spell
            if target * spell < success:
                target += 1
            self.find_target_position(potions, target, res)
        return res
    
    def find_target_position(self, potions, target, res):
        left = 0
        right = len(potions)-1
        if target <= potions[0]:
            res.append(len(potions))
            return 
        if target > potions[-1]:
            res.append(0)
            return
        while left < right:
            mid = int((left + right + 1) / 2)
            if potions[mid] < target:
                left = mid
            else:
                right = mid - 1
        res.append(len(potions) - left - 1)
        
# @lc code=end

