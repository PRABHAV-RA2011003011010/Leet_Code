class Solution:
    def reverseBits(self, n: int) -> int:
        binstr=format(n, '032b')
        

        return int(binstr[::-1],2)
        