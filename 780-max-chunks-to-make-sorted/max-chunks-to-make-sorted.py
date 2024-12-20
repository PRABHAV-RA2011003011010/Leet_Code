class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxseen=0
        chunks=0
        for i,num in enumerate(arr):

            maxseen=max(num,maxseen)

            if maxseen==i:
                chunks+=1


        return chunks
        