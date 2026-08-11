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
    int res = 0;

    public int height(TreeNode root) {
        if (root == null) return 0;

        int hL = this.height(root.left);
        int hR = this.height(root.right);

        this.res = Math.max(this.res, hL+hR);
        return 1 + Math.max(hL, hR);
    }

    public int diameterOfBinaryTree(TreeNode root) {
        this.height(root);

        return this.res;
    }
}