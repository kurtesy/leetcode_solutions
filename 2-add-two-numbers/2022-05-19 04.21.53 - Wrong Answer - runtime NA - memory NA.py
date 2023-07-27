# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root1 = l1
        p1 = None
        while l1 and l2:
            temp = l1.val + l2.val + carry
            l1.val = temp%10
            carry = temp//10
            p1 = l1
            l1 = l1.next
            l2 = l2.next
        if carry > 0 and p1:
            newNode = ListNode(carry)
            p1.next = newNode
        return root1
            