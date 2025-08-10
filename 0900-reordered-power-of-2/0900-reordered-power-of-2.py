class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        powers=[]
        valid_len_powers=[]
        for i in range(30):
            powers.append(str(2**i))
        for power in powers:
            if len(power)==len(str(n)):
                valid_len_powers.append(power)

        original_count=defaultdict(int)
        for char in str(n):
            original_count[char]+=1

   

        for power in valid_len_powers:
            cur_count=defaultdict(int)
            for char in power:
                cur_count[char]+=1
            if original_count==cur_count:
                return True
        return False



        

        

       

        
        