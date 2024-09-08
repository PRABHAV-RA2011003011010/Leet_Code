# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res=[]
        if not head:
            while len(res)<k:
                res.append(None)
            return res
        cur = head
        count=0
        while cur:
            cur=cur.next
            count+=1
        n=count//k
        ext=count%k
        cur=head
        count1=0
        res.append(head)

        while ext and cur:
            count1+=1
            if count1==n+1:
                next1=cur.next
                cur.next= None
                cur=next1
                if cur:
                    res.append(cur)
                ext-=1
                count1=0
            else:
                cur=cur.next

        while cur:
            count1+=1
            if count1==n:
                next1=cur.next
                cur.next= None
                cur=next1
                if cur:
                    res.append(cur)
                count1=0
            else:
                cur=cur.next 
        
        while len(res)<k:
            res.append(None)        


        return res
        