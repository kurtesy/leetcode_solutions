# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        p1 = None
        res = ListNode()
        root = res
        while l1 or l2:
            v1 = 0 if not l1 else l1.val
            v2 = 0 if not l2 else l2.val
            s = v1+v2+carry
            rem = s%10
            res.next = ListNode(rem)
            carry = s//10
            if l1:l1 = l1.next
            if l2:l2 = l2.next
            res = res.next
        if carry > 0:
            res.next = ListNode(carry)
        return root.next
            