class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        res=[float('inf')]*(amount+1)

        res[0]=0



        for coin in coins:

            for cur in range(coin,amount+1):

                res[cur]=min(res[cur],res[cur-coin]+1)
        
        return res[-1] if res[-1]!=float('inf') else -1




        

       
        