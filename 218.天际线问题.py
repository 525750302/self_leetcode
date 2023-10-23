#
# @lc app=leetcode.cn id=218 lang=python
#
# [218] 天际线问题
#

# @lc code=start
from sortedcontainers import SortedKeyList
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        stack_up = SortedKeyList()
        stack_down = SortedKeyList()

        for i in range(len(buildings)):
            stack_up.add([buildings[i][0],buildings[i][2]])
            stack_down.add([buildings[i][1],buildings[i][2]])
        height = 0
        b_stack = [0]
        result = []
        location = 0
        while stack_down or stack_up:
            flag = 0
            if stack_up:
                if stack_up[0][0] <= stack_down[0][0]:
                    location = stack_up[0][0]
                    while stack_up and stack_up[0][0] == location:
                        b_stack.append(stack_up[0][1])
                        if height < stack_up[0][1]:
                            flag = 1
                            height = stack_up[0][1]
                        stack_up.pop(0)
                    if flag == 1:
                        result.append([location,height])
                else:
                    location = stack_down[0][0]
                    while stack_down and stack_down[0][0] == location:
                        b_stack.remove(stack_down[0][1])
                        if height > max(b_stack):
                            flag = 1
                            height = max(b_stack)
                        stack_down.pop(0)
                    if flag == 1:
                        result.append([location,height])
            else:
                location = stack_down[0][0]
                while stack_down and stack_down[0][0] == location:
                    b_stack.remove(stack_down[0][1])
                    if height > max(b_stack):
                        flag = 1
                        height = max(b_stack)
                    stack_down.pop(0)
                if flag == 1:
                    result.append([location,height])
        return result

# @lc code=end

