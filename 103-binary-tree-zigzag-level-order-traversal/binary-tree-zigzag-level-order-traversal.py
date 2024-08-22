# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        zig=[]
        if not root:
            return zig
        q=deque()
        q.append(root)
        rev=0
        while(q):
            n=len(q)
            lvl=[]
            
            for _ in range(n):
                popped=q.popleft()
                lvl.append(popped.val)

                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            if rev:
                zig.append(lvl[::-1])
                rev=0
            else:
                zig.append(lvl)
                rev=1

        return zig
        