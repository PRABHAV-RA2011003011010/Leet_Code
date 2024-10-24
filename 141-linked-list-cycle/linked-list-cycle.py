# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        li=[]
        while head:
            li.append(head)
           
            if head.next in li:
                return True
            
            head=head.next

        return False