class Solution:
    def totalNQueens(self, n: int) -> int:
        col=set()
        diagonal=set()
        antidiagonal=set()
        row=0
        count=0

        def backtrack(r):
            nonlocal count
            if r==n:
                count+=1
                return 
            
            for c in range(n):
                dia=r-c
                anti=r+c
                if c not in col and dia not in diagonal and anti not in antidiagonal:
                    col.add(c)
                    diagonal.add(dia)
                    antidiagonal.add(anti)

                    backtrack(r+1)

                    col.remove(c)
                    diagonal.remove(dia)
                    antidiagonal.remove(anti)

        backtrack(row)
        return count
        