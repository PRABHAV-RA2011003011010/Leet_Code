class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for x in tokens:
            
            if x=="+":
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op2+op1)
            elif x=="-":
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op2-op1)
            elif x=="*":
                op1=stack.pop()
                op2=stack.pop()
                stack.append(op2*op1)
            elif x=="/":
                op1=stack.pop()
                op2=stack.pop()
                stack.append(int(op2/op1))
            else:
                stack.append(int(x))
        
        return stack[0]
        