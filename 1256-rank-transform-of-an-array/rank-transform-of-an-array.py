class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        sort_arr=arr.copy()
        sort_arr.sort()
        dict1={}
        rank=0

        for num in sort_arr:
            if num not in dict1:
                rank+=1
                dict1[num]=rank
        for i in range(len(arr)):
            arr[i]=dict1[arr[i]]

        return arr
        