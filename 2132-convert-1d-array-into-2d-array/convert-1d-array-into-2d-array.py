class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        arr2d=[]
        row=[]
        if not len(original)==m*n:
            return arr2d

        for x in original:
            row.append(x)
            if len(row)==n:
                arr2d.append(row)
                row=[]

        return arr2d