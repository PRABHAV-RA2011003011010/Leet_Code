class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        n=len(fruits)
        res=0
        for i in range(n):
            for j in range(n):
                if fruits[i]<=baskets[j]:
                    res+=1
                    baskets[j]=0
                    break
                
        return n-res       



        
        
        