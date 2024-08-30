# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque()
        q.append(root)
        
        maxsum=float('-inf')
        curlvl=0
        lvl=0
        while(q):
            lvlsum=0
            curlvl+=1
            for _ in range(len(q)):
                popped=q.popleft()
                lvlsum+=popped.val
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)

            if lvlsum>maxsum:
                lvl=curlvl
                maxsum=lvlsum
        return lvl

            


        