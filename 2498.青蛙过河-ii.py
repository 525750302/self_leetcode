#
# @lc app=leetcode.cn id=2498 lang=python
#
# [2498] 青蛙过河 II
#

# @lc code=start
class Solution(object):
    def maxJump(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        left = 0
        right = stones[-1]

        while left < right:
            mid = (left + right - 1) // 2
            if self.check(stones,mid):
                right = mid
            else:
                left = mid + 1
        
        return right
    
    def check(self,stones,distace):
        used = [0] * len(stones)
        last = stones[0]
        target = -1
        for times in range(2):
            i = 1
            while i < len(stones):
                #print(times,i, distace,target,last,stones[last] + distace,stones[-1])
                if used[i] == 0 and stones[i] - stones[last] <= distace:
                    target = i
                elif stones[i] - stones[last] > distace:
                    if target == -1:
                        return False
                    else:
                        last = target
                        used[target] = 1
                        if stones[last] + distace >= stones[-1]:
                            target = -1
                            last = stones[0]
                            break
                        target = -1
                        i -= 1
                elif i == len(stones)-1 and stones[last] + distace < stones[-1]:
                    return False
                i += 1
        return True

# @lc code=end

