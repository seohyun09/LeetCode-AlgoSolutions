# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.diameter=0

        def dfs(node):
            if not node:
                return 0
            
            left=dfs(node.left)
            right=dfs(node.right)

            self.diameter=max(self.diameter, left, right)

            if node.left and node.right and node.val==node.left.val and node.val==node.right.val:
                self.diameter=max(self.diameter, left+right+2)
                return max(left, right)+1
            if node.left and node.val==node.left.val:
                return left+1
            if node.right and node.val==node.right.val:
                return right+1
            return 0

        return max(dfs(root), self.diameter)