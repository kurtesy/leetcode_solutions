# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root
        found = None
        self.result = []
        while cur:
            if cur.val == val:
                found = cur
                break
            left = cur.left
            right = cur.right
            if left and val < cur.val:
                cur = left
            if right and val < cur.val:
                cur = right
        return found
        