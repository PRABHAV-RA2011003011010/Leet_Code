class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        gifts=[-x for x in gifts]
        heapify(gifts)
        while k:
            cur=heapq.heappop(gifts)
            cur=math.floor(math.sqrt(-cur))
            heapq.heappush(gifts,-cur)
            k-=1

        return -sum(gifts)
        
        

