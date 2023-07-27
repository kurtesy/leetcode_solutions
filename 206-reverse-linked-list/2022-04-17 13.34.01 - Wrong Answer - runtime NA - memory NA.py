# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            if prev:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            else:
                temp = head.next
                head.next = None
                prev = head
                head = temp
            print(prev)
            if not head.next:
                break
        return prev
                