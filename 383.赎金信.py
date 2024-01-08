#
# @lc app=leetcode.cn id=383 lang=python
#
# [383] 赎金信
#

# @lc code=start
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        a = {}
        b = {}
        for i in ransomNote:
            a[i] = a.get(i,0)+1

        for i in magazine:
            b[i] = b.get(i,0)+1
        for i in a:
            if i not in b or b[i]<a[i]:
                return False
        
        return True
# @lc code=end

