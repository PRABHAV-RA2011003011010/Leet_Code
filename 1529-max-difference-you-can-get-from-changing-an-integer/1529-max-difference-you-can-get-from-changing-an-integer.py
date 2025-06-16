class Solution:
    def maxDiff(self, num: int) -> int:
        str_num=str(num)
        max_swap=0
        min_swap=0
        max_str=""
        min_str=""

        for i in range(len(str_num)):
            if str_num[i]!='9':
                max_swap=str_num[i]
                break
        if str_num[0]!='1':
            min_swap=str_num[0]
        else:
            for i in range(1,len(str_num)):
                if str_num[i]!='0' and str_num[i]!='1':
                    min_swap=str_num[i]
                    break
        for i in range(len(str_num)):
            if str_num[i]==max_swap:
                max_str+='9'
            else:
                max_str+=str_num[i]
        if str_num[0]!='1':

            for i in range(len(str_num)):
                if str_num[i]==min_swap:
                    min_str+='1'
                else:
                    min_str+=str_num[i]
        else:
            min_str+='1'
            for i in range(1,len(str_num)):
                if str_num[i]==min_swap:
                    min_str+='0'
                else:
                    min_str+=str_num[i] 
        
        return int(max_str)-int(min_str)