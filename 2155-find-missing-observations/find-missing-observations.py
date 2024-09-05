class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum1=0
        m=len(rolls)
        missing_rolls=[]
        for roll in rolls:
            sum1+=roll
        unknown_sum=mean*(n+m)-sum1
        if (unknown_sum/n)>6 or (unknown_sum/n)<1 :
            return missing_rolls
        while n:
            curroll=unknown_sum//n
            missing_rolls.append(curroll)
            unknown_sum-=curroll
            n-=1

        return missing_rolls

        