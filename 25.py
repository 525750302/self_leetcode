# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        save_data = []
        left = head
        right = head
        while right != None:
            for i in range(k):
                if right == None:
                    return head
                save_data.append(right.val)
                right = right.next
            while left!=right:
                left.val = save_data.pop()
                left = left.next
        
        return head