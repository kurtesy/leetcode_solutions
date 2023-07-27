# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = 0
        self.maxLvl = 0
        queue=deque()
        queue.append(root)
        lst=[]
        lvl = 0
        while queue:
            levels=[]
            for i in range(len(queue)):
                node=queue.popleft()
                if node:
                    levels.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if levels:
                lvl+=1
                s = sum(levels)
                if s>self.maxSum:
                    print(s,self.maxSum, lvl)
                    self.maxSum = s
                    self.maxLvl = lvl
        return self.maxLvl
            
