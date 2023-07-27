# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root, res = []):
        if not root:
            return
        self.inorderTraversal(root.left, res)
        res.append(root.val)
        self.inorderTraversal(root.right, res)
        return res
        