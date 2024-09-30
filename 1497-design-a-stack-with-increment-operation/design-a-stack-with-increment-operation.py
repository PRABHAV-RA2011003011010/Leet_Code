class CustomStack:

    def __init__(self, maxSize: int):

        self.stack=[0]*maxSize
        self.size=maxSize
        self.top=-1
        

    def push(self, x: int) -> None:

        if self.top==self.size-1:
            return
        self.top+=1
        self.stack[self.top]=x
        

    def pop(self) -> int:
        if self.top==-1:
            return -1
        popped=self.stack[self.top]
        self.top-=1
        return popped
        

    def increment(self, k: int, val: int) -> None:
        if self.top>=k-1:
            m=k-1
        else:
            m=self.top
        for x in range(m+1):
            self.stack[x]+=val

    
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)