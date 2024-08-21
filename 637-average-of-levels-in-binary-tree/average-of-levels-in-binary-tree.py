# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    
        avg=[]
        if not root:
            return avg
        q=deque()
        q.append(root)
        while(q):
            sum=0
            n=len(q)
            for _ in range(n):
                popped=q.popleft()

                sum+=popped.val
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            avg.append(sum/n)
        return avg
            
        