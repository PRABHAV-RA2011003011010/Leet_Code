# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tra=[]
        if not root:
            return tra
        q=deque()
        q.append(root)
        while q:
            n=len(q)
            lvl=[]
            for _ in range(n):
                popped=q.popleft()
                lvl.append(popped.val)

                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            tra.append(lvl)
        return tra
        