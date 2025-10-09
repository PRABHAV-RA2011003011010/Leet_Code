class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]

        for bracket in s:
            if stack and ((stack[-1]=="(" and bracket==")") or (stack[-1]=="[" and bracket=="]") or (stack[-1]=="{" and bracket=="}")):
               
                stack.pop()      
            else:
                stack.append(bracket)

        return False if stack else True
        