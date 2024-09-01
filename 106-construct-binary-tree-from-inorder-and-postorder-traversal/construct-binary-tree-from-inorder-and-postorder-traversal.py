# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.cur=-1
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
        
        root=TreeNode()
        root.val=postorder[self.cur]
        self.cur-=1
        for x in range(len(inorder)):
            if inorder[x]==root.val:
                break
        root.right=self.buildTree(inorder[x+1:],postorder)
        root.left=self.buildTree(inorder[:x],postorder)
        


        return root
        