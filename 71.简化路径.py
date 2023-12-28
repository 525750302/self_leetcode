#
# @lc app=leetcode.cn id=71 lang=python
#
# [71] 简化路径
#

# @lc code=start
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        file = ""
        for i in path[1:]:
            if i == "/":
                if file == "..":
                    if stack:
                        stack.pop()
                elif file != "." and file != "":
                    stack.append(file)
                file = ""
            else:
                file += i
        if file == "..":
            if stack:
                stack.pop()
        elif file != "." and file != "":
            stack.append(file)
            
        
        res = ""
        for i in stack:
            res += "/" + i

        return res if stack else "/"

# @lc code=end

