# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.res = {}
    def fn(self,root, r,c, d):
        if root:
            d[c].append((r,root.val))
            self.fn(root.left,r+1, c-1,d)
            self.fn(root.right,r+1, c+1,d)
    def verticalTraversal(self, root):
        d = defaultdict(list)
        self.fn(root,0,0,d)
        ans=[]
        for i in sorted(d.keys()):
            temp=[]
            for j in sorted(d[i]):
                temp.append(j[1])
            ans.append(temp)
        return ans
        
        