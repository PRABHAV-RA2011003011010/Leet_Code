class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        traverse=[]
        rows=len(mat)
        cols=len(mat[0])
        res=[]

        for i in range(rows):
            for j in range(cols):
                traverse.append([i+j,mat[i][j]])

        sorted_lst = sorted(traverse, key=lambda x: x[0])
        print(sorted_lst)
        temp=[]
        for pair in sorted_lst:
            if pair[0]%2==0:
                temp.append(pair[1])
            else:
                for i in range(len(temp)-1,-1,-1):
                    res.append(temp[i])
                temp=[]
                res.append(pair[1])
        if temp:
            for i in range(len(temp)-1,-1,-1):
                    res.append(temp[i])

        return res
                