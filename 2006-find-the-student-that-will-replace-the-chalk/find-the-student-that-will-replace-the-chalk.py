class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i=0
        sum1=sum(chalk)
        k=k%sum1


        while k>=chalk[i]:

            k=k-chalk[i]
            if k<0:
                break
            i+=1
            i%=len(chalk)

        return i

    
        