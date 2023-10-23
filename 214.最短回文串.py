#
# @lc app=leetcode.cn id=214 lang=python
#
# [214] 最短回文串
#

# @lc code=start
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r_words = []
        words = []
        location = [-1]*len(s)
        for i in range(len(s)):
            r_words.append(s[i])
            words.append(s[len(s) - 1 - i])
        for i in range(1,len(s)):
            last = location[i-1]
            while last >-1 and s[i]!=s[last+1]:
                last = location[last]
            if s[i] == s[last+1]:
                location[i] = last + 1
        print(location)
        p1 = -1
        p2 = -1
        for i in range(len(s)):
            p1 +=1
            p2 += 1
            while r_words[p1]!=words[p2]:
                p1 = location[p1 - 1] + 1
                if p1 == 0 and r_words[p1]!=words[p2]:
                    p1 = -1
                    break
        result = ""
        for i in range(len(s)):
            result = result + words[i]
        for i in range(p1+1,len(s)):
            result = result + r_words[i]

        return result
# @lc code=end
