# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0

        def dfs(node):
            nonlocal diameter
            if not node:
                return (-1, 0)
            
            left, left_value=dfs(node.left)
            right, right_value=dfs(node.right)

            if diameter<left+right+2:
                diameter=left+right+2

            return (max(left, right)+1, left+right+2)
        
        state, value=dfs(root)
        return max(state, value, diameter)