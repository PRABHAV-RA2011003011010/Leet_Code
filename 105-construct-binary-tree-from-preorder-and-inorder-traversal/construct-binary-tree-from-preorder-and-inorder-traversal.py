# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cur = 0 
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not inorder:
            return
        
        root=TreeNode()
        root.val=preorder[self.cur]
        self.cur+=1
        for x in range(len(inorder)):
            if inorder[x]==root.val:
                break

        root.left=self.buildTree(preorder,inorder[:x])
        root.right=self.buildTree(preorder,inorder[x+1:])


        return root

        