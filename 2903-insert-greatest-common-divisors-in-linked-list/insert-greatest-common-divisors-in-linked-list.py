# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        prev=head
        cur=head.next

        while cur:

            new_node=ListNode()
            new_node.val=math.gcd(cur.val,prev.val)
            prev.next=new_node
            new_node.next=cur
            prev=cur
            cur=cur.next
    
        return head
        