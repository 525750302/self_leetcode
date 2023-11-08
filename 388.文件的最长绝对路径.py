#
# @lc app=leetcode.cn id=388 lang=python
#
# [388] 文件的最长绝对路径
#

# @lc code=start
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        paths = input.split('\n')
        max_len = 0
        stack = [0]
        pre = 0
        for path in paths:
            depth = path.count('\t')
            while depth < len(stack) - 1:
                stack.pop()
            pre = stack[-1]
            stack.append(pre + len(path) - depth)
            if depth != 0:
                stack[-1] += 1
            #print(stack)
            if '.' in path:
                max_len = max(max_len, stack[-1])

        return max_len
# @lc code=end

