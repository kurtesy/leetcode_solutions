# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        cur = head
        while cur:
            length+=1
            cur = cur.next
        target = length - n
        ctr = 1
        cur = head
        print(target)
        if length == 1:
            return None
        if target == 0:
            head = head.next
            return head
        while cur and ctr < target:
            cur = cur.next
            ctr += 1
        self.deleteNode(cur)
        return head

    def deleteNode(self, node):
        if node.next and not node.next.next:
            node.next = None
        if node.next and node.next.next:
            node.next = node.next.next