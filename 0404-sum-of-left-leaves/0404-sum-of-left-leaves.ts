/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function sumOfLeftLeaves(root: TreeNode | null): number {
    let dfs = (node: TreeNode | null, sum: number, is_left: boolean): number => {
        if(!node) return 0;

        if(!node.left && !node.right && is_left)
            return sum += node.val;
        
        return dfs(node.left, sum, true) + dfs(node.right, sum, false)
    }

    return dfs(root, 0, false);
};