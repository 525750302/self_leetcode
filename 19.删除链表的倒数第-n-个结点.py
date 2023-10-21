#
# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        point = head
        line = []
        while point != None:
            line.append(point)
            point = point.next
        
        length = len(line)
        if n == length:
            head = head.next
        else:
            line[length - n - 1].next = line[length - n].next
        
        return head
        
# @lc code=end

