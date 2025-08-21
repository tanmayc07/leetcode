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

function sumRootToLeaf(root: TreeNode | null): number {
    let sum: number = 0;

    let dfs = (node: TreeNode | null, path: number) => {
        if(node !== null) {
            path = (path<<1) | node.val;
            if(!node.left && !node.right) {
                sum += path;
            }
            dfs(node.left, path)
            dfs(node.right, path);
        }
    }

    // Accumulate the binary numbers in lst
    dfs(root, 0)
    
    return sum;
};