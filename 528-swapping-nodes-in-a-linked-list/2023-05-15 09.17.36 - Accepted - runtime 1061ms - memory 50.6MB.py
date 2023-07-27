# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        first = head
        ctr = 1
        while cur:
            if ctr == k:
                first = cur
                break
            ctr+=1
            cur = cur.next
        second = head
        cur = first
        while cur.next:
            cur = cur.next
            second = second.next
        first.val, second.val = second.val, first.val
        # print(first.val, second.val)
        return head