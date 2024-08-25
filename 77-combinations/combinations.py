class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        sol=[]

        def backtrack(s):
            if len(sol)==k:
                res.append(sol[:])
                return

            for x in range(s,n+1):
                if x not in sol:
                    sol.append(x)
                    backtrack(x+1)
                    sol.pop()
        backtrack(1)
        return res