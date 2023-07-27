# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.res = {}
    def verticalTraversal(self, root, ref = 0, ok=False):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        cur = root
        if ref in self.res:
            self.res[ref].append(cur.val)
        else:
            self.res[ref] = [cur.val]
        if cur.left:
            self.verticalTraversal(cur.left, ref-1, True)
        if cur.right:
            self.verticalTraversal(cur.right, ref+1, True)
        if not ok:
            return [v for k, v in sorted(self.res.items())]
        
        