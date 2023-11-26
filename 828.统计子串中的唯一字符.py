#
# @lc app=leetcode.cn id=828 lang=python
#
# [828] 统计子串中的唯一字符
#

# @lc code=start
class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_position = {}
        llast_position = {}
        ans = 0
        for i in range(len(s)):
            target = s[i]
            if target in last_position.keys():
                ans += i - last_position[target]
                llast_position[target] = last_position[target]
                last_position[target] = i
            else:
                llast_position[target] = -1
                last_position[target] = i
                ans += last_position[target] - llast_position[target]
            for j in last_position.keys():
                if j == target:
                    continue
                ans += last_position[j] - llast_position[j]
        
        return ans 


# @lc code=end

