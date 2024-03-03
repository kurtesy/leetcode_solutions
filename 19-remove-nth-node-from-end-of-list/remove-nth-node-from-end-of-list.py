# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length+=1
            cur = cur.next
        cur = head
        index = length - n
        prev = None
        while index > 0:
            prev = cur
            cur = cur.next
            index -= 1
        print(length, cur, prev)
        if prev is None :
            head = cur.next
        elif cur.next is None and prev.next is None:
            head = None
        else:
            prev.next = cur.next
        return head
        