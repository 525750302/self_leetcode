#
# @lc app=leetcode.cn id=769 lang=python
#
# [769] 最多能完成排序的块
#

# @lc code=start
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        stack = []
        ans = 0
        for i in range(len(arr)):
            if arr[i] == i and len(stack) == 0:
                ans += 1
            else:
                if arr[i] != i:
                    if arr[i] not in stack:
                        stack.append(arr[i])
                    else:
                        stack.remove(arr[i])
                    
                    if i not in stack:
                        stack.append(i)
                    else:
                        stack.remove(i)
                        if len(stack) == 0:
                            ans += 1
        return ans 
# @lc code=end

