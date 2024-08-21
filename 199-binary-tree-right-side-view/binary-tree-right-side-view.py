# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        r=[]
        if not root:
            return r
        q=deque()
        q.append(root)
        while(q):
            n=len(q)
            lastnode=q[-1]
            r.append(lastnode.val)
            for _ in range(n):
                popped=q.popleft()

                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            
        return r
        