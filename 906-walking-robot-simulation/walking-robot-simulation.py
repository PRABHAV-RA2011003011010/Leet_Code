class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        x=0
        y=0
        directions=("north","east","south","west")
        curdir=0
        distance=0
        obstacles1=set((i,j) for i,j in obstacles)


        for command in commands:
            curdistance=0

            if command==-1:
                curdir+=1
                curdir%=4
            elif command==-2:
                curdir-=1
                curdir%=4
                
            else:

                if directions[curdir]=="north":
                    for i in range(command):
                        y+=1
                        if (x,y) in obstacles1:
                            y-=1
                            break
                elif directions[curdir]=="east":
                    for i in range(command):
                        x+=1
                        if (x,y) in obstacles1:
                            x-=1
                            break
                    
                elif directions[curdir]=="south":
                    for i in range(command):
                        y-=1
                        if (x,y) in obstacles1:
                            y+=1
                            break
                    
                elif directions[curdir]=="west":
                    for i in range(command):
                        x-=1
                        if (x,y) in obstacles1:
                            x+=1
                            break
                    
        
        
            curdistance=x**2+y**2
            distance=max(curdistance,distance)
        

        
        return distance
        


        