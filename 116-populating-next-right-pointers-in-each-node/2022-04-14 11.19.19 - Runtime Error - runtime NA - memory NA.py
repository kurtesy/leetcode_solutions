"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = []
        queue.append(root)
        res = []
        while queue:
            cur = queue.pop(0)
            if cur.left:
                if cur.right:
                    cur.left.next = cur.right
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
                if cur.next:
                    cur.right.next = cur.next.left
                queue.append(cur.right)
        return root
        
        
        