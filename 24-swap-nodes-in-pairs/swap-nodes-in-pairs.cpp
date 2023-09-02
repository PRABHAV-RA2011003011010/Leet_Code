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
    ListNode* swapPairs(ListNode* head) {
        ListNode *prev=head,*cur=head;
        while(cur && cur->next){
            if(cur==head){
                head=cur->next;
                cur=head;
                

            }
            else{
                prev->next=cur->next;
                prev=cur;
                cur=cur->next;
               

            }
            prev->next=cur->next;
                cur->next=prev;
                cur=prev->next;

        }


        
   return head; }
};