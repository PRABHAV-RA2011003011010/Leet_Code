# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        lesser_dummy = ListNode()
        greater_dummy = ListNode()

        lesser_tail = lesser_dummy
        greater_tail = greater_dummy

      

        cur=head

        while cur:

            if cur.val<x:
                lesser_tail.next=cur
                lesser_tail=lesser_tail.next
            
            else:
                greater_tail.next=cur
                greater_tail=greater_tail.next
            
            cur=cur.next
        
        lesser_tail.next = greater_dummy.next
        greater_tail.next=None

        return lesser_dummy.next


                
                


        