class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        sum_cost = sum(cost)
        sum_gas = sum(gas)
       
        if sum_cost > sum_gas:
            return -1
        res=0
        cur_tank=0
        for start in range(n):
            cur_tank += gas[start]-cost[start]
            
            if cur_tank<0:
                res=start+1
                cur_tank=0

        return res

               

