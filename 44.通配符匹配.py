#
# @lc app=leetcode.cn id=44 lang=python
#
# [44] 通配符匹配
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[0]*(1+len(s))for i in range((len(p)+1))]
        dp[0][0] = 1
        for i in range(1,len(p)+1):
            target = p[i-1]
            if target == "*":
                for j in range(len(s) + 1):
                    if dp[i-1][j] == 0:
                        continue
                    for k in range(j, len(s) + 1):
                        dp[i][k] = 1
                    break
            elif target == "?":
                for j in range(len(s)):
                    if dp[i-1][j] == 0:
                        continue
                    dp[i][j+1] = dp[i-1][j]
            else:
                for j in range(len(s)):
                    if dp[i-1][j] == 0:
                        continue
                    if s[j] == target:
                        dp[i][j+1] = dp[i-1][j]
        
        if dp[len(p)][len(s)] == 1:
            return True
        else:
            return False
            
# @lc code=end

