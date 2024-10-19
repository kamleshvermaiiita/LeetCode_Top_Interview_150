# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        index = -1
        inorder_map = {value: idx for idx, value in enumerate(inorder)}

        def helper(left, right):
            nonlocal index
            if left > right:
                return None

            curr = postorder[index]
            index -= 1
            node = TreeNode(curr)

            if left == right:
                return node

            inorder_index = inorder_map[curr]
            node.right = helper(inorder_index + 1, right)
            node.left = helper(left, inorder_index - 1)

            return node

        return helper(0, len(inorder) - 1)
        