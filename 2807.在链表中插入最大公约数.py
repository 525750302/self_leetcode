#
# @lc app=leetcode.cn id=2807 lang=python
#
# [2807] 在链表中插入最大公约数
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        point1 = head
        if point1.next == None:
            return head
        point2 = head.next
        while point2 != None:
            new_node = ListNode(self.gcd(point1.val, point2.val))
            point1.next = new_node
            new_node.next = point2
            point1 = point2
            point2 = point2.next
        return head
    
    def gcd(self, a, b):
    # Compute the greatest common divisor of a and b
        while b != 0:
            a, b = b, a % b
        return a


# @lc code=end

