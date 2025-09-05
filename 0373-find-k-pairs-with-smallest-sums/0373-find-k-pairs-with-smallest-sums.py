class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap=[]
        res=[]
        for num1 in nums1:
            
            min_heap.append((num1+nums2[0],num1,0))
            
        heapq.heapify(min_heap)
        for _ in range(k):
            sum,i,j=heapq.heappop(min_heap)
            res.append([i,nums2[j]])
            if j+1<len(nums2):
                heapq.heappush(min_heap,(i+nums2[j+1],i,j+1))
        return res


        