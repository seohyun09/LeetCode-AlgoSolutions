# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node1, node2):
            if not node1: return
            if not node2: return

            if node1.left and node2.left:
                node1.left.val+=node2.left.val
                dfs(node1.left, node2.left)
            if node1.right and node2.right:
                node1.right.val+=node2.right.val
                dfs(node1.right, node2.right)

            if not node1.left and node2.left:
                node1.left=TreeNode(node2.left.val)
                dfs(node1.left, node2.left)
            if node1.left and not node2.left:
                dfs(node1.left, node2.left)

            if not node1.right and node2.right:
                node1.right=TreeNode(node2.right.val)
                dfs(node1.right, node2.right)
            if node1.right and not node2.right:
                dfs(node1.right, node2.right)
        
        if not root1 and root2:
            return root2
        if root1 and not root2:
            return root1
        if not root1 and root2:
            return None
        if root1 and root2:
            root1.val+=root2.val

        dfs(root1, root2)
        return root1
            



