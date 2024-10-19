# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if (not root) or (not root.left and not root.right):
            return True
        
        return self.sametree(root.left, root.right)
        
    def sametree(self, rootleft, rootright):
        if not rootleft and not rootright:
            return True
        if not rootleft or not rootright:
            return False
        return rootleft.val == rootright.val and self.sametree(rootleft.left, rootright.right) and self.sametree(rootleft.right, rootright.left)
        
        
                
        