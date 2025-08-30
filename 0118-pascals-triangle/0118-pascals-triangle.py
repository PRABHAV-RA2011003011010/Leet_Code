class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        res.append([1])
        if numRows==1:
            return res
        
        res.append([1,1])
        if numRows==2:
            return res

        for i in range(numRows-2):
            cur=[]
            prev=res[-1]
            print(prev)
            cur.append(1)
            for j in range(len(prev)-1):
                cur.append(prev[j]+prev[j+1])
            cur.append(1)
            res.append(cur)
        return res

        