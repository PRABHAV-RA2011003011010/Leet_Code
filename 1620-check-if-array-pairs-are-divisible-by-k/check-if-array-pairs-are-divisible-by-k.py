class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n=len(arr)
        freq=defaultdict(int)

        for num in arr:
            freq[num%k]+=1

        if freq[0]%2==1:
            return False
        for i in range(1,k//2+1):

            if freq[i]!=freq[k-i]:
                return False

        return True





        
        