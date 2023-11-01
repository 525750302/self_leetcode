class Solution:
    def check(self,s,i,j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        
        return i +1, j -1

    def longestPalindrome(self, s: str) -> str:
        result_left = 0
        result_right = 0
        for i in range(len(s)):
            left1, right1 =self.check(s,i,i)
            left2, right2 = self.check(s,i,i+1)
            if right1 - left1 > result_right - result_left:
                result_right = right1
                result_left = left1
            if right2 - left2 > result_right - result_left:
                result_right = right2
                result_left = left2
        
        return s[result_left:result_right + 1]