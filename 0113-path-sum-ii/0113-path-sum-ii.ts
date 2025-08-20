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

function pathSum(root: TreeNode | null, targetSum: number): number[][] {
    if(!root) return [];
    let res: number[][] = [];
    
    let dfs = (node: TreeNode, sm: number, lst: number[]) => {
        if(!node) return;
        lst.push(node.val);

        if(!node.left && !node.right && sm === targetSum) {
            res.push([...lst]);
        } else {
            dfs(node.left, sm+(node.left?.val ?? 0), lst)
            dfs(node.right, sm+(node.right?.val ?? 0), lst)
        }

        lst.pop();
    }

    dfs(root, root.val, []);
    return res;
}; 