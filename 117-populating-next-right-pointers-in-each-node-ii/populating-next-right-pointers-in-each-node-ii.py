"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque()
        q.append(root)
        dummy=Node(-999) 
        while q:
            length=len(q) 
            
            prev=None
            for _ in range(length): 
                popped=q.popleft()
                if not prev:
                    prev=popped
                else:
                    prev.next=popped
                    prev=prev.next
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
                
            
            
        return root