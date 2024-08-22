# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        q=deque()
        q.append(root)
        depth=0
        while(q):
            n=len(q)
            depth+=1
        
            for _ in range(n):
                popped=q.popleft()

                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            
        return depth
        