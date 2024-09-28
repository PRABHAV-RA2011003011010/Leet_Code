class MyCircularDeque:

    def __init__(self, k: int):

        self.q=[0]*k
        self.front=0
        self.last=-1
        self.k=k
        self.size=0
        
        
    def insertFront(self, value: int) -> bool:
        
        if self.isFull():
            return False
        self.front=(self.front-1)%self.k
        self.q[self.front]=value
        self.size+=1
        return True
        
        

    def insertLast(self, value: int) -> bool:

        if self.isFull():
            return False
        self.last=(self.last+1)%self.k
        self.q[self.last]=value
        self.size+=1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front=(self.front+1)%self.k
        self.size-=1
        
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.last=(self.last-1)%self.k
        self.size-=1
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.last]
        

    def isEmpty(self) -> bool:

        return True if (self.size==0) else False
        

    def isFull(self) -> bool:

        return True if (self.size==self.k) else False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()