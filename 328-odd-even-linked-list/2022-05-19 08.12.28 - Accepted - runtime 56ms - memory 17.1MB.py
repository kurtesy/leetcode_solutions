# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        resOdd = ListNode()
        resEven = ListNode()
        evenRoot = resEven
        oddRoot = resOdd
        idx = 0
        while head:
            v = head.val
            if idx%2==0:
                resOdd.next = ListNode(v)
                resOdd = resOdd.next
            else:
                resEven.next = ListNode(v)
                resEven = resEven.next
            idx+=1
            head = head.next
        resOdd.next = evenRoot.next
        return oddRoot.next
        
        
            