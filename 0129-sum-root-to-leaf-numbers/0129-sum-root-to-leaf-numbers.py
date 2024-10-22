# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, path):
            nonlocal total
            if not root:
                return
            if not root.left and not root.right:
                total += path*10 + root.val
                return
            if root.left:
                dfs(root.left, path*10 + root.val)
            if root.right:
                dfs(root.right, path*10 + root.val)
            
        
        total = 0
        dfs(root, 0)
        return total
            
        