#
# @lc app=leetcode.cn id=2487 lang=python
#
# [2487] 从链表中移除节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack = []
        point = head
        while point:
            while stack and stack[-1] < point.val:
                stack.pop()
            stack.append(point.val)
            point = point.next
        begin = ListNode(0)
        new_node = begin
        last = begin
        for i in stack:
            new_node.val = i
            new_node.next = ListNode(0)
            last = new_node
            new_node = new_node.next
        last.next = None
        return begin


# @lc code=end

