# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high, s=0):
        cur = root
        if low<=cur.val<=high:
            s += cur.val
        if cur.left:
            s = self.rangeSumBST(cur.left, low, high, s)
        if cur.left:
            s = self.rangeSumBST(cur.right, low, high, s)
        return s