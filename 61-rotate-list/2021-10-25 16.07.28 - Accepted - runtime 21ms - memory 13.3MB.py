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
        if not cur:
            return head
        while cur.next:
            length+=1
            cur = cur.next
        cur.next = head
        # print(cur, length)
        cur = head
        rotLen = (length-(k%length))-1
        for i in range(rotLen):
            cur = cur.next
        head = cur.next
        cur.next = None
        return head
        
            
        