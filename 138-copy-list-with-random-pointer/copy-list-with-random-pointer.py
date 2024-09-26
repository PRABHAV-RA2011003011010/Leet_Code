"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        head2=Node(head.val)
        cur1=head
        cur2=head2
    
        dict1={
            None:None
        }
        dict1[cur1]=cur2

        cur1=cur1.next
        

        while cur1:

            cur2.next=Node(cur1.val)
            cur2=cur2.next
            dict1[cur1]=cur2

            cur1=cur1.next

        cur1=head
        cur2=head2

        while cur1:
            cur2.random=dict1[cur1.random]
            cur1=cur1.next
            cur2=cur2.next





        return head2


            


            
        