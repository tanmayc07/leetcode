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

    public int calc(TreeNode root) {
        if (root == null) return 0;
        int l = this.calc(root.left);
        int r = this.calc(root.right);

        this.res += Math.abs(l-r);
        return l + r + root.val;
    }

    public int findTilt(TreeNode root) {
        this.calc(root);
        return this.res;
    }
}