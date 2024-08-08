# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        first=head
        last1=head
        l=1
        while(last1.next):
                last1=last1.next
                l+=1
        k=k%l
        while(k):
            last1=first

            while(last1.next.next):
                last1=last1.next
            last2=last1.next
            last1.next=None
            last2.next=first
            first=last2
            k=k-1
        return first
        