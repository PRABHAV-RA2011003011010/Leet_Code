# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        x=0
        y=0
        x1=0
        y1=1

        while head:

            matrix[x][y]=head.val

            if not 0<=y+y1<n or not 0<=x+x1<m or matrix[x+x1][y+y1]!=-1:

                x1,y1=y1,-x1

            x+=x1
            y+=y1
            head=head.next
        return matrix

            





            

        
    
        