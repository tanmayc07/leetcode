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
    
    let st: [TreeNode, number][] = [];
    let res: boolean = false;

    st.push([root, root.val]);

    while(st.length > 0) {
        let [node, sm] = st.pop();

        if(node.left === null && node.right === null && sm === targetSum) {
            res = true;
            break;
        }
        else {
            if(node.left !== null) st.push([node.left, sm+node.left.val]);
            if(node.right !== null) st.push([node.right, sm+node.right.val]);
        }
    }

    return res;
};