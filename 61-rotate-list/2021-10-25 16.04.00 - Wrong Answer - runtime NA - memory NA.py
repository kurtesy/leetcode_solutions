# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
            :type head: ListNode
            :type k: int
            :rtype: ListNode
        """
        cur = head
        length = 1
        while cur.next:
            length+=1
            cur = cur.next
        cur.next = head
        # print(cur, length)
        cur = head
        for i in range(length-k-1):
            cur = cur.next
        head = cur.next
        cur.next = None
        return head
        
            
        