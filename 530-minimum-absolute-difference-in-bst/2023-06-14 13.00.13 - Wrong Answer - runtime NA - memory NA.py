# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        cur = root
        res = 10**7
        while cur.left:
            lv = cur.val - cur.left.val
            res = min(res, lv)
            cur = cur.left
        while cur.right:
            rv = cur.right.val - cur.val
            res = min(res, rv)
            cur = cur.right
        return res