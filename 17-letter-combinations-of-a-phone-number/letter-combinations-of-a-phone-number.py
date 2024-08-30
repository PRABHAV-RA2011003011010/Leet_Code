class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        temp=""
        if len(digits)==0:
            return res
        phone={
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz"    
        }

        def backtrack(index):
            nonlocal temp
            if len(digits)==len(temp):
                res.append(temp)
                return
            for char in phone[digits[index]]:
                temp+=char
                backtrack(index+1)
                temp=temp[:-1]
                

        
        backtrack(0)
        return res


        