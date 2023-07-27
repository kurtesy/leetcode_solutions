# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        mid = self.findMid(head)
        head2 = mid.next
        head2 = self.reverse(head2)
        cur = head
        while head2 != None:
            if head2.val != cur.val:
                return False
            head2 = head2.next
            cur = cur.next
        return True
            
        
    def findMid(self, head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse(self, t):
        cur = t
        prev = None
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
        