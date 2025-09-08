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

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    if (list1 === null && list2 === null) return null;

    let lst = [];
    while (list1 !== null && list2 !== null) {
        if (list1.val <= list2.val) { 
            lst.push(list1.val);
            list1 = list1.next;
        } else {
            lst.push(list2.val);
            list2 = list2.next;
        }
    }

    while (list1 !== null) {
        lst.push(list1.val);
        list1 = list1.next;
    }

    while (list2 !== null) {
        lst.push(list2.val);
        list2 = list2.next;
    }


    let newHead = new ListNode(lst[0], null);
    let curr = newHead;
    for (let i=1; i<lst.length; i++) {
        curr.next = new ListNode(lst[i], null);
        curr = curr.next;
    }

    return newHead;
};