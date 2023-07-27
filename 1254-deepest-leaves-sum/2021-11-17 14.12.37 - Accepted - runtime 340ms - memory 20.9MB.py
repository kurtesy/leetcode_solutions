# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def dfs(self, cur, height, s, level):
        if not cur:
            return s
        s += cur.val if level == height-1 else 0
        # print(cur.val, level, s)
        s = self.dfs(cur.left, height, s, level+1)
        s = self.dfs(cur.right, height, s, level+1)
        return s
    
    def deepestLeavesSum(self, root,):
        height = self.treeHeight(root,0)
        res = self.dfs(root, height, 0, 0)
        return res
        
    def treeHeight(self, root, height):
        if not root:
            return height
        leftHeight = self.treeHeight(root.left, height+1)
        rightHeight = self.treeHeight(root.right, height+1)
        return max(leftHeight, rightHeight)
        
        
        