/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int[] preorder;
    private int[] inorder;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        this.inorder = inorder;
        return dfs(0, 0, inorder.length);
    }

    private TreeNode dfs(int p_start, int i_start, int i_end) {
        if (p_start >= preorder.length || i_start >= i_end) {
            return null;
        }

        int node_val = preorder[p_start];
        TreeNode node = new TreeNode(node_val);

        for (int i = i_start; i < i_end; i++) {
            if (inorder[i] == node_val) {
                node.left = dfs(p_start + 1, i_start, i);
                node.right = dfs(p_start + (i - i_start) + 1, i + 1, i_end);
                break;
            }
        }
            return node;
        }
}