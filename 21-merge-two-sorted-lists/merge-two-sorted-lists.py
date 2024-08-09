# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1==None):
            return list2
        elif(list2==None):
            return list1
        cur1=list1
        prev=list1
        cur2=list2
        next2=list2
        head=list1
        while(cur1 and cur2):

            if(cur1.val>=cur2.val):
                next2=cur2.next
                if(cur1==prev):
                    cur2.next=prev
                    if(head==list1):
                        head=cur2
                    prev=cur2
                    cur2=next2
                    continue
                else:
                    prev.next=cur2
                    cur2.next=cur1
                    prev=prev.next
                    cur2=next2
                    continue

            if(cur1==prev):
                cur1=cur1.next
            else:
                cur1=cur1.next
                prev=prev.next
            if(cur1==None and cur2!=None):
                prev.next=cur2
        
        return head
        
        