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
            if not cur.left and not cur.right:
                break
            if cur.left and val < cur.val:
                cur = cur.left
            if cur.right and val > cur.val:
                cur = cur.right
            print(cur.val)
        return found