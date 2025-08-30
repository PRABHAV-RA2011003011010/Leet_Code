class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:

        dict=defaultdict(int)
        n=len(basket1)
        for i in range(n):
            dict[basket1[i]]+=1
            dict[basket2[i]]+=1
        for i in dict:
            if dict[i]%2!=0:
                return -1
            else:
                dict[i]=dict[i]//2


        req=[]
        not_req=[]

        for i in range(n):
            if dict[basket1[i]]==0:
                not_req.append(basket1[i])
                continue
            dict[basket1[i]]-=1
        for i in dict:
            if dict[i]!=0:
                req.extend([i]*dict[i])
        req.sort()
        not_req.sort(reverse=True)
        res=0
        global_min = min(basket1 + basket2)

        for i in range(len(req)):
            res += min(2 * global_min, min(req[i], not_req[i]))
      
        return res
            


        