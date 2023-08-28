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
    ListNode* deleteMiddle(ListNode* head) {
        ListNode *slow=head,*prev=head,*temp=head;
        if(!temp || !temp->next){
            head=0;
            return head;
        }
        while(temp && temp->next){
            prev=slow;
            slow=slow->next;
            temp=temp->next->next;
            
}
     prev->next=slow->next;
        


        
    return head;}
};