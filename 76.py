class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = {}
        value_num = 0
        for i in range(len(t)):
            if dic.get(t[i]) == None:
                dic[t[i]] = 1
                value_num = value_num + 1
            else:
                dic[t[i]] += 1
        
        left = -1
        right = 0
        result_left = -1
        result_right = -1
        min_result = 99999
        def cal(left,right):
            nonlocal dic,value_num,min_result,result_left,result_right
            if dic.get(s[right]) ==None:
                right += 1
                left += 1
            while right < len(s):
                if dic.get(s[right]) != None:
                    dic[s[right]] -= 1
                    if dic[s[right]] == 0:
                       value_num -= 1
                if value_num == 0:
                    while value_num == 0 and left < right-1:
                        if dic.get(s[left+1]) != None:
                            if dic[s[left+1]] < 0:
                                dic[s[left+1]] += 1
                            elif dic[s[left+1]] == 0:
                                break
                        left += 1
                    if min_result>right - left:
                        min_result = right-left
                        result_right = right
                        result_left = left
                    while value_num <= 1 and left < right-1:
                        left += 1
                        if dic.get(s[left]) != None:
                            if dic[s[left]] == 0:
                                value_num += 1
                            dic[s[left]] += 1
                        if value_num == 1 and dic.get(s[left+1]) != None:
                            if dic[s[left+1]] >= 0:
                                break
                right += 1
            return result_left,result_right
        result_left,result_right = cal(left,right)
        if result_left == -1 and result_right == -1:
            return ""
        else:
            return s[result_left+1:result_right+1]

            

        