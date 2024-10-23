# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        q=deque()
        q.append([root,root.val])

        while q:
            lvlsum=0
            for node,csum in q:
                lvlsum+=node.val

            for _ in range(len(q)):
                childsum=0
                popped,localsum=q.popleft()

                if popped.left:
                    childsum+=popped.left.val
                
                if popped.right:
                    childsum+=popped.right.val
                
                if popped.left:
                    q.append([popped.left,childsum])
                
                if popped.right:
                    q.append([popped.right,childsum])
                
                popped.val=lvlsum-localsum
        
        return root
                
                
                  





        