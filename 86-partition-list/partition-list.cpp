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
        ListNode* temp=head,*less=0,*gre=0,*head1=0,*head2=0;
         head1= new ListNode(0); 
        less=head1;
        head2= new ListNode(0);
        gre=head2;
        

       

        while(temp){
            if((temp->val)<x){
               
                    less->next=temp;
                    less=temp;
                
            }
            else{
                
                    gre->next=temp;
                    gre=temp;
                }


            
        temp=temp->next;}
        gre->next=0;
        less->next=head2->next;
        
    return head1->next;}
};