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
        if(head==NULL || head->next==NULL){
            return head;
        }
        ListNode *res=new ListNode(0);
        ListNode *cur=head,*prev=res;
        
        while(cur){
            bool dup=false;
            while(cur->next && cur->val==cur->next->val){
                cur=cur->next;
                dup=true;
            }
            if(!dup){
                prev->next=cur;
                prev=cur;
            }
            cur=cur->next;
        }
        prev->next=0;
        
    return res->next;}
};