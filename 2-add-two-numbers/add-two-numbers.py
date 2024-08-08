# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1=""
        num2=""
        cur=l1
        while cur:
            num1+=str(cur.val)
            cur=cur.next
        cur=l2
        while cur:
            num2+=str(cur.val)
            cur=cur.next
        num1=num1[::-1]
        num2=num2[::-1]
        sum=str(int(num1)+int(num2))
        sum=sum[::-1]
        print(sum)
        
        head=None
        for x in sum:
            new_node=ListNode(int(x),None)
            if(head==None):
                head=new_node
            else:
                cur=head
                while(cur.next):
                    cur=cur.next
                cur.next=new_node
        return head



            


        
        
        
