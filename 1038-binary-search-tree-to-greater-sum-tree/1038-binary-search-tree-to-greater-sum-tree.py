# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sumValue=0
        node=root

        def inorder(node):
            if node:
                inorder(node.right)
                self.sumValue+=node.val
                node.val=self.sumValue
                inorder(node.left)
        
        inorder(node)
        return root