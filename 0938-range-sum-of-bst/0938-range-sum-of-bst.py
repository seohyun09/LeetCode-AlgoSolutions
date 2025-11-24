# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.answer=0

        def recursive(node):
            if not node: return
            if low<=node.val<=high:
                self.answer+=node.val
            recursive(node.left)
            recursive(node.right)
        
        recursive(root)
        return self.answer