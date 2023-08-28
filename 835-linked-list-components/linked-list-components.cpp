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
    int numComponents(ListNode* head, vector<int>& nums) {
        bool com=false;
        int tot=0;
        while(head){
            if(count(nums.begin(), nums.end(), head->val) && com==false){
                com=true;
                tot++;
                }
            else if(!count(nums.begin(), nums.end(), head->val)){
                com=false;

            }
            head=head->next;


        }







       return tot;}
};