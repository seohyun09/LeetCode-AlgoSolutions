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
    int difference = Integer.MAX_VALUE;
    int prev = -1;

    public int minDiffInBST(TreeNode root) {
        inorder(root);
        return difference;    
    }
    
    private void inorder(TreeNode node) {
        if (node == null) return;

        inorder(node.left);
        if (prev != -1) {
            difference = Math.min(difference, node.val-prev);
        }

        prev = node.val;
        inorder(node.right);
    }
}