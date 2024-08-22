class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        temp=""
        for x in path:
            if x!='/':
                temp+=x
            else:
                if temp==".." and stack:
                    stack.pop()
                    
                elif temp and temp!="." and temp!="..":
                    stack.append(temp)
                temp=""
        if temp==".." and stack:
            stack.pop()
                    
        elif temp and temp!="." and temp!="..":
            stack.append(temp)

        final=""
        for x in stack:
            final+='/'+ x
        if not stack:
            final+='/'

        return final
        