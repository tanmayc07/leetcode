/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        int len=0;
        ListNode start = head;
        
        while(start != null) {
            len++;
            start=start.next;
        }
        
        int mid = len/2;
        for(int i=0; i<mid; i++) {
            head=head.next;
        }
        
        return head;
    }
}