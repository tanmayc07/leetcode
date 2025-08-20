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

function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
    if(!root) return false;
    
    let dfs = (node: TreeNode, sm: number): boolean => {
        if(node !== null) {
            if(node.left === null && node.right === null)
                return sm === targetSum;
            else {
                let leftHas = node.left ? dfs(node.left, sm + node.left.val) : false;
                let rightHas = node.right ? dfs(node.right, sm + node.right.val) : false;
                return leftHas || rightHas;
            }
        }
        return false;
    }

    return dfs(root, root.val);
};