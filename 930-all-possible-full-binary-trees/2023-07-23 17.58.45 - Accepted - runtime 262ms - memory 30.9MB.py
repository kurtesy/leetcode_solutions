# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0: return []
        if N == 1: return [TreeNode(0)]
        res = []
        for i in range(1, N, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(N - 1 - i):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)
        return res