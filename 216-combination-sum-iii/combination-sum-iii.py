class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        sum=0
        res=[]
        com=[]

        def backtrack(start,sum):
            if sum==n and len(com)==k:
                sum=0
                res.append(com[:])
                return
            if len(com)==k:
                return
            
            for num in range(start,10):
                if num not in com:
                    com.append(num)
                    sum+=num
                    backtrack(num+1,sum)
                    sum-=num
                    com.pop()


        backtrack(1,sum)
        return res
                


        