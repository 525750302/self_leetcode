#
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
#

# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        count = 0
        max_result = 0
        for i in range(len(s)):
            if s[i] =="(":
                if len(stack)>0 and (stack[-1] == "(" or stack[-1] == ")"):
                    stack.append(0)
                stack.append(s[i])
            else:
                count = 0
                while len(stack)>0 and (stack[-1] != "(" and stack[-1] != ")"):
                    count += stack[-1]
                    stack.pop()
                if len(stack)>0 and stack[-1] == "(":
                    stack.pop()
                    count += 2
                    while len(stack)>0:
                        if (stack[-1] != "(" and stack[-1] != ")"):
                            count += stack[-1]
                            stack.pop()
                            continue
                        if stack[-1] == "(":
                            stack.append(count)
                            break
                        elif stack[-1] == ")":
                            stack.append(count)
                            break
                    if len(stack) == 0:
                        stack.append(count)

                    max_result = max(max_result, count)
                else:
                    stack.append(s[i])
        return max_result

# @lc code=end

