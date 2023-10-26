#
# @lc app=leetcode.cn id=30 lang=python
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        stack = []
        data_flow = []
        window = len(words)
        w_length = len(words[0])
        if window > int(len(s) / w_length):
            return []
        for i in range(w_length):
            for begin_point in range(int(len(s) / w_length)):
                begin = begin_point * w_length + i
                for j in range(len(words)):
                    if self.check(words[j],begin,s):
                        data_flow.append(j+1)
                        break
                    if j == len(words) - 1:
                        data_flow.append(-1)
            stack.append(data_flow)
            data_flow = []
        dic = {}
        require = {}
        for i in range(len(words)):
            dic[words[i]] = 0
        for i in range(len(words)):
            dic[words[i]] = dic[words[i]] + 1
        for i in range(len(words)):
            require[i+1] = dic[words[i]]
        flag = 0
        result = []
        for i in range(w_length):
            target = stack[i]
            for k in range(len(words)):
                dic[k+1] = 0
            flag = 0
            for j in range(window):
                if target[j] == -1:
                    continue
                dic[target[j]] += 1
                if dic[target[j]] == require[target[j]]:
                    flag  += require[target[j]]
                if flag == len(words):
                    result.append(i)
            j = window
            #print(flag)
            while j <len(target):
                if target[j - window ]!= -1:
                    dic[target[j - window ]] -= 1
                    if dic[target[j - window ]] == require[target[j - window ]] -1:
                        flag -= require[target[j - window ]]
                if target[j]!= -1:
                    dic[target[j]] += 1
                    if dic[target[j]] == require[target[j]]:
                        flag += require[target[j]]
                j += 1
                if flag == len(words):
                    result.append(i + w_length*(j-window))

        return result
        
    
    def check(self,pat,begin,s):
        for i in range(len(pat)):
            if begin + i >= len(s):
                return False
            if s[begin + i] != pat[i]:
                return False
        
        return True

# @lc code=end

