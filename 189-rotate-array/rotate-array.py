class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        
        n=len(nums)
        k=k%n-1
        def rev(l,r,arr):
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
        rev(0,n-1,nums)
        rev(0,k,nums)
        rev(k+1,n-1,nums)
        
        


        
        
        