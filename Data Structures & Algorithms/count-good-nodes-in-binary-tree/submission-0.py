# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,value):
            if not node:
                return 0
            res = 1 if  node.val>= value else 0
            value = max(value,node.val)
            res += dfs(node.left,value)
            res += dfs(node.right,value)
            return res
        
        return dfs(root,root.val)