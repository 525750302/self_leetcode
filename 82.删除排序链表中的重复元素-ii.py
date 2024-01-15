#
# @lc app=leetcode.cn id=82 lang=python
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dic = {}
        last = head
        while head:
            dic[head.val] = dic.get(head.val, 0) + 1
            head = head.next
        head = last
        last = None
        res = last
        while head:
            if dic[head.val] == 1:
                if last == None:
                    last = head
                    res = last
                    head = head.next
                else:
                    last.next = head
                    last = head
                    head = head.next
            else:
                head = head.next
        if last:
            last.next = None
        
        return res
                


        
# @lc code=end

