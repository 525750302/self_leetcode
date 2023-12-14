#
# @lc app=leetcode.cn id=2130 lang=python
#
# [2130] 链表最大孪生和
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        for i in range(len(stack) // 2):
            stack[i] += stack[-i - 1]
        return max(stack)

# @lc code=end

