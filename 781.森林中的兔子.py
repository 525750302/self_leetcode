#
# @lc app=leetcode.cn id=781 lang=python
#
# [781] 森林中的兔子
#

# @lc code=start
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        dic = {}
        res = 0
        for i in answers:
            if i not in dic:
                dic[i] = 1
                res += i + 1
            else:
                dic[i] += 1
                if dic[i] > i + 1:
                    res += i + 1
                    dic[i] = 1
        return res
# @lc code=end

