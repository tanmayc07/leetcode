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

function countNodes(root: TreeNode | null): number {
    if(root === null) return 0;
    if(root.left === null && root.right === null) return 1;

    function leftHeight(node: TreeNode): number {
        if(node === null) return 0;
        else return 1 + leftHeight(node.left);
    }

    function rightHeight(node: TreeNode): number {
        if(node === null) return 0;
        else return 1 + rightHeight(node.right);
    }

    let lh = leftHeight(root);
    let rh = rightHeight(root);
    if(lh !== rh) {
        let dq = [];
        let cnt = 0;

        dq.push(root);
        while(dq.length > 0) {
            let curr = dq.shift();
            if(curr !== null) {
                cnt += 1;
                if(curr.left !== null) dq.push(curr.left);
                if(curr.right !== null) dq.push(curr.right);
            }
        }
        return cnt;
    } else {
        return Math.pow(2, lh)-1;
    }

};