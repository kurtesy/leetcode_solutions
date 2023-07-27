# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        cur1 = root1
        cur2 = root2
        if not cur1 or not cur2:
            return cur1
        s = cur1.val + cur2.val
        cur1.val = s
        print(s)
        if cur1.left and cur2.left:
            self.mergeTrees(cur1.left, cur2.left)
        if cur1.right and cur2.right:
            self.mergeTrees(cur1.right, cur2.right)
        if cur2.left and not cur1.left:
            cur1.left = cur2.left
        if cur2.right and not cur1.right:
            cur1.right = cur2.right
        return cur1
            
            
        