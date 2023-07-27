# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def middle( temp):
        slow =  temp
        fast = temp
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
def reverse(t):
    cur = t
    prev = None
    while cur is not None:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

class Solution:
    def isPalindrome(self, head):
        cur = head
        mid = middle(head)
        last = reverse(mid)
        while last is not None:
            if last.val != cur.val:
                return False
            last =last.next
            cur =cur.next
        return True