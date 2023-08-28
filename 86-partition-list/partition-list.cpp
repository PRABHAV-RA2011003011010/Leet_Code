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
    ListNode* partition(ListNode* head, int x) {
        ListNode *less,*gre,*head1,*head2;
         head1= new ListNode(0); 
        less=head1;
        head2= new ListNode(0);
        gre=head2;
        

       

        while(head){
            if((head->val)<x){
               
                    less->next=head;
                    less=head;
                
            }
            else{
                
                    gre->next=head;
                    gre=head;
                }


            
        head=head->next;}
        gre->next=0;
        less->next=head2->next;
        
    return head1->next;}
};