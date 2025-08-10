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

function preorderTraversal(root: TreeNode | null): number[] {
    let tree: number[] = [];
    let stack: TreeNode[] = [];

    stack.push(root);
    while(stack.length !== 0) {
        let curr: TreeNode = stack.pop();
        if(curr !== null) {
            tree.push(curr.val);
            if(curr.right !== null) {
                stack.push(curr.right);
            }
            if(curr.left !== null) {
                stack.push(curr.left);
            }
        }
    }

    return tree;
};