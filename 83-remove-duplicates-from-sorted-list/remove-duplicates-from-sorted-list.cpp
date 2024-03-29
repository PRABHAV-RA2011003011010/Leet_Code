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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *cur=head,*prev=head;
        while( head && prev->next){
            if(cur==head){
                cur=prev->next;
            }
            if(prev->val==cur->val){
                prev->next=cur->next;
            }
            else{
                prev=cur;

            }
            cur=cur->next;

        }

        
    return head;}
};