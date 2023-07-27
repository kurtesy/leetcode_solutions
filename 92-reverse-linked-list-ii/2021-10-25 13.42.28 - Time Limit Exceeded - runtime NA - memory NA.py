# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        pos = 1
        cur = head
        if left == right:
            return head
        prev = cur
        rightNode = None
        while cur:
            print(pos, left, right)
            if pos == right:
                rightNode = cur.next
            cur = cur.next
            pos+=1
        pos = 1
        cur = head
        while cur:
            print(pos, left, right)
            if pos == left:
                revHead = cur
                revNode = self.reverse(revHead, right-left, rightNode)
                prev.next = revNode
            pos+=1
            prev = cur
            cur = cur.next
        return head
    def reverse(self, node, dist, rightNode):
        prev = None
        current = node
        ctr = 0
        while(current is not None and ctr <= dist):
            next = current.next
            current.next = prev
            prev = current
            current = next
            ctr+=1
        temp = prev
        while temp.next:
            temp = temp.next
        temp.next = rightNode
        return prev
            