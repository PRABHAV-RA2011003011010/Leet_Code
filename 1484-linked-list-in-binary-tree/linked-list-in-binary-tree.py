# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root or not head:
            return False
          
        def dfs(root):
            if not root:
                return False
            if root.val==head.val and trav(root,head): 
                return True
            return dfs(root.left) or dfs(root.right)
            
            

        def trav(node,cur):
            if not cur:
                return True
            if not node:
                return False
            
            if node.val!=cur.val:
                return False
                
            return trav(node.left,cur.next) or trav(node.right,cur.next)
    
        return dfs(root)
        
        