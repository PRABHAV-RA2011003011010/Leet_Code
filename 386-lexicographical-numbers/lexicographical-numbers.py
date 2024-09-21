class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res=[]

        for num in range(1,n+1):
            res.append(str(num))
        res.sort()
        res = [int(x) for x in res]

        return res

        