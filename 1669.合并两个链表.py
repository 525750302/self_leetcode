# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        point = list1
        for i in range(b):
            if i == a - 1:
                left = point
            point = point.next
        right = point.next
        left.next = list2
        point = list2
        while point.next!=None:
            point = point.next
        point.next = right
        return list1

            
        