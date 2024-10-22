# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        q=deque()
        lvlsum=[]

        q.append(root)

        while q:

            sum1=0
            lvl=len(q)
            for _ in range(lvl):

                popped=q.popleft()
                sum1+=popped.val

                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)

            lvlsum.append(sum1)
        if len(lvlsum)<k:
            return -1
        lvlsum=[-x for x in lvlsum]

        heapq.heapify(lvlsum)
        while k>1:
            heapq.heappop(lvlsum)
            k-=1
        

        return -heapq.heappop(lvlsum)


        