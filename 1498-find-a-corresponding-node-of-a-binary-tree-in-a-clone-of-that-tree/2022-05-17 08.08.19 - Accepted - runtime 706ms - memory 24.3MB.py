# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.ans = None
        self.parseTree(cloned, target)
        return self.ans
    def parseTree(self, root, target):
        if not root:
            return
        if root.val == target.val:
            self.ans = root
        self.parseTree(root.left, target)
        self.parseTree(root.right, target)
        