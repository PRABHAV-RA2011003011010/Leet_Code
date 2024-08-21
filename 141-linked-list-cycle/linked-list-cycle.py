# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        cur=head
        li=[]
        while cur:
            li.append(cur)
           
            if cur.next in li:
                return True
            
            cur=cur.next

        return False