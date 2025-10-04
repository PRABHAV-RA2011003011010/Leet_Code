class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        profit_max_heap=[]
        capital_min_heap=[]

        for i in range(len(profits)):
            heapq.heappush(capital_min_heap,(capital[i],profits[i]))
        print(capital_min_heap)

        for _ in range(k):

            while capital_min_heap and capital_min_heap[0][0]<=w:
                cap,pro=heapq.heappop(capital_min_heap)
                heapq.heappush(profit_max_heap,-pro)
            
            if not profit_max_heap:
                break

            cur_pro=heapq.heappop(profit_max_heap)
            w+=-cur_pro

        return w


        