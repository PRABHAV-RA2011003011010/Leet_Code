class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res=[]
        state=[]
        sum=0

        def backtrack(start,sum):
            if sum==target:
                res.append(state[:])
                return
            if sum>target:
                return
            
            for num in range(start,len(candidates)):
                sum+=candidates[num]
                state.append(candidates[num])

                backtrack(num,sum)

                state.pop()
                sum-=candidates[num]


        backtrack(0,sum)
        return res
                



    
    

        