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

function levelOrder(root: TreeNode | null): number[][] {
    let tree = []
    let dq = []

    if(root === null) return []

    dq.push(root)
    while(dq.length !== 0) {
        let same_level = []
        let level_size = dq.length;

        for(let i=0; i<level_size; i++) {
            let curr = dq.shift();
            if(curr !== null) {
                same_level.push(curr.val);
                if(curr.left !== null) dq.push(curr.left);
                if(curr.right !== null) dq.push(curr.right);
            }
        }
        tree.push(same_level)
    }

    return tree;
};