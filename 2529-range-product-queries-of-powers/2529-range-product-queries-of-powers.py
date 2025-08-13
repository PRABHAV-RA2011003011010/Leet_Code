class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        powers=[]
        res=[]
        modulo=10*9+7
        
        binary = format(n, 'b')
        
        for i in range(len(binary)):
            if binary[len(binary)-i-1]=='1':
                powers.append(2**i)
        print(powers)
        for query in queries:
            product=1
            for i in range(query[0],query[1]+1):
                product = product*powers[i]% (10**9 + 7)
            
            res.append(product)

        return res
