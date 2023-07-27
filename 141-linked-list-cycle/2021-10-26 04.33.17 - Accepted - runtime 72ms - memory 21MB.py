# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head
        visited = set()
        while cur:
            if cur in visited:
                return True
            visited.add(cur)
            cur = cur.next
        return False