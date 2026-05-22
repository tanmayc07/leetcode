/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* dum = head;
        ListNode* prev = nullptr;

        while (dum != nullptr) {
            ListNode* temp = dum->next;
            dum->next = prev;
            prev = dum;
            dum = temp;
        }

        return prev;
    }
};