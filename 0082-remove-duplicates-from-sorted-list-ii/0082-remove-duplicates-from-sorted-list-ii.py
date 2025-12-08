# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev=dummy
        cur=head

        while cur:
            if cur.next and cur.val==cur.next.val:
                while cur.next and cur.val==cur.next.val:
                    cur=cur.next
                cur=cur.next
                prev.next=cur
            else:
                prev.next=cur
                prev=prev.next
                cur=cur.next

        head=dummy.next  

        return head
        