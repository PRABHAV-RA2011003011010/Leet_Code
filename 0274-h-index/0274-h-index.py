class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        for i in range(len(citations),0,-1):
            cur=0
            for j in range(len(citations)):
                if citations[j]>=i:
                    cur+=1
                if cur==i:
                    return i
        return 0