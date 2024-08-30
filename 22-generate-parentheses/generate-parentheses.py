class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res=[]
        state=""
        reslen=n*2
        parenthesis=['(',')']

        def valid(str1):
            stack=[]
            for x in str1:
                if x=='(':
                    stack.append(x)
                elif x==')' and not stack:
                    return False
                else:
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        return False
            if stack:
                return False
            else:
                return True



        def backtrack():
            nonlocal state
            if len(state)==reslen:
                if valid(state):
                    res.append(state)
                return
            
            for x in parenthesis:
                state+=x
                backtrack()
                state=state[:-1]
        backtrack()
        return res