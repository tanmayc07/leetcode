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

function binaryTreePaths(root: TreeNode | null): string[] {
    let st: [TreeNode, string][] = [];
    let res: string[] = [];

    st.push([root, "" + root.val]);

    while(st.length > 0) {
        let [node, path] = st.pop();
        
        if(node.left === null && node.right === null) {
            res.push(path);
        } else {
            if(node.left !== null)
                st.push([node.left, path+"->"+node.left.val]);
            if(node.right !== null)
                st.push([node.right, path+"->"+node.right.val]);
        }
    }
    return res;
};