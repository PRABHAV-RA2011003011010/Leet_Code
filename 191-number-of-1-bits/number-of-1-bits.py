class Solution:
    def hammingWeight(self, n: int) -> int:

        binary=bin(n)
        res=0
        for bit in binary:
            if bit=='1':
                res+=1
        return res
        