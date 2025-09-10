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

function swapNodes(head: ListNode | null, k: number): ListNode | null {
    let start = head;
    let n = 0;
    while (start) {
        n++;
        start = start.next;
    }
    let pass = n-k;
    let kFromStart = head;
    while (k-- > 1) kFromStart = kFromStart.next;
    let kFromEnd = head;
    while (pass-- > 0) kFromEnd = kFromEnd.next;

    let t = kFromStart.val;
    kFromStart.val = kFromEnd.val;
    kFromEnd.val = t;
      
    return head;
};