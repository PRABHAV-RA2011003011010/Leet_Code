class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        res=""
        length=max(len(a),len(b))
        a = a.zfill(length)
        b = b.zfill(length)
        for n1 in range(len(a)-1,-1,-1):
            
            cur=int(a[n1])+int(b[n1])+carry
            if cur==2:
                carry=1
                res="0"+res
            elif cur==3:
                carry=1
                res="1"+res
            else:
                res=str(cur)+res
                carry=0
        if carry :
            res=str(carry)+res
        return res
            

        