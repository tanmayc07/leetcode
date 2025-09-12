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

function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    if (!head || !head.next) return null;
    let len = 0;
    let start = head;

    while (start) {
        len++;
        start = start.next;
    }
    
    if (n==len) return head.next;

    start = head;
    for(let i=1; i<(len-n); i++)
        start = start.next;

    start.next = start.next?.next;
    return head;
};