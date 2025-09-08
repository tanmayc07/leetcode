/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function reverseList(head: ListNode | null): ListNode | null {
    let root = head;
    let lst = [];
    while (root !== null) {
        lst.push(root.val);
        root = root.next;
    }
    lst.reverse();
    root = head;
    lst.forEach ((val) => {
        root.val = val;
        root = root.next;
    });
    return head;
};