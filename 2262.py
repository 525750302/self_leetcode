class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        save_data = [-1 for i in range(26)]

        result = 0
        addvalue = 0
        for i in range(len(s)):
            addvalue = addvalue + i - save_data[int(ord(s[i]) - ord("a"))]
            result = result + addvalue
            save_data[int(ord(s[i]) - ord("a"))] = i 
        
        return result