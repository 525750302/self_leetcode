#
# @lc app=leetcode.cn id=2744 lang=python
#
# [2744] 最大字符串配对数目
#

# @lc code=start
class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for i in range(len(words)):
            stack  = []
            for j in range(len(words[i])):
                stack.append(words[i][j])
            for j in range(i+1,len(words)):
                save = stack[0::]
                for k in range(len(words[j])):
                    if save and save[-1] == words[j][k]:
                        save.pop()
                    else:
                        break
                if len(save) == 0:
                    res += 1
        
        return res 

# @lc code=end

