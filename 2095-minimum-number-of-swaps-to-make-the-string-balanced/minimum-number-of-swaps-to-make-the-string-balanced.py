class Solution:
    def minSwaps(self, s: str) -> int:
        cur=0
        swaps=0

        for char in s:

            if char=='[':
                cur+=1
            else:
                cur-=1
            
            if cur==-1:
                swaps+=1
                cur+=2
                
        return swaps   
        