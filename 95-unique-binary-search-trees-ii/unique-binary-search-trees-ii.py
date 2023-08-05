# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        ini_list = [i for i in range(1, n+1)]

        def build(cur_list):
            if len(cur_list) == 1:
                return [TreeNode(cur_list[0])]
            else:
                result = []
                for i in range(len(cur_list)):
                    if i == 0:
                        rs = build(cur_list[i+1:])
                        for r in rs:
                            node = TreeNode(cur_list[i])
                            node.right = r
                            result.append(node)
                    elif i == len(cur_list)-1:
                        ls = build(cur_list[:i])
                        for l in ls:
                            node = TreeNode(cur_list[i])
                            node.left = l
                            result.append(node)
                    else:
                        ls, rs = build(cur_list[:i]), build(cur_list[i+1:])
                        for l in ls:
                            for r in rs:
                                node = TreeNode(cur_list[i])
                                node.left = l
                                node.right = r
                                result.append(node)
                
                return result
        return build(ini_list)
