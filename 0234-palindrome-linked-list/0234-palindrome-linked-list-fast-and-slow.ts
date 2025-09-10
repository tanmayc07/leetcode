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

function isPalindrome(head: ListNode | null): boolean {
    let slow = head;
    let fast = head;

    // find the middle
    while (fast && fast.next) {
        fast = fast.next.next;
        slow = slow.next;
    }

    // reverse the second half
    let curr = slow;
    let prev = null;
    while (curr) {
        let temp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = temp;
    }

    // Compare first half and second half
    let start = head;
    while (prev) {
        if (prev.val !== start.val) return false;
        // console.log(`${prev.val} ${start.val}`);
        prev = prev.next;
        start = start.next;
    }

    return true;
};