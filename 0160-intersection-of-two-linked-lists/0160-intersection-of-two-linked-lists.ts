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

function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
    if (!headA && !headB) return null;

    let a = headA;
    let b = headB;
    while (a !== b) {
        if (a) a = a.next;
        else a = headB;

        if (b) b = b.next;
        else b = headA;
    }

    return a;
};