# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        result = ListNode()

        if len(lists) == 0:
            return result
        
        listnum = len(lists)

        numcount = [0] * 2 * 10000

        for i in range(listnum):
            a = lists[i]
            while a is not None:
                numcount[a.val + 10000] = numcount[a.val + 10000] + 1
                a = a.next

        for i in range(2*10000):
            for j in range(numcount[i]):
                result.append(i - 10000)
        
        return result
    
a = Solution()
input = [[]]
result = a.mergeKLists(input)
print(result)