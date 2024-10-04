class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        n=len(skill)
        pairs=int(n/2)
        total_skills=sum(skill)
        value_of_pair=total_skills/pairs
        value=int(value_of_pair)
        res=0
        if value_of_pair!=value:
            return -1

        freq=defaultdict(int)
        for num in skill:
            freq[num]+=1

        for num in skill:
            if freq[value-num]>0:
                res+=num*(value-num)
                freq[value-num]-=1
            else:
                return -1
        
        return int(res/2)
        