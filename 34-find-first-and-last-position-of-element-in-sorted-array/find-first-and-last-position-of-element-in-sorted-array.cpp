class Solution {
private:
   int binarys(vector<int>& nums,int f,int l,int t){
       if (l >= f){
       int mid = l + f / 2;
       if(nums[mid]==t)
       return mid;
       else if(t>nums[mid]){
           return binarys(nums,mid+1,l,t);}
        else if(t<nums[mid]){
            return binarys(nums,f,mid-1,t);

        
       }}
   return -1;}


public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int>temp;
        int pos=binarys(nums,0,nums.size()-1,target);
        int star=pos,en=pos;
        if(pos!=-1){
        for(int i=pos;i<nums.size()-1;i++){
            if(nums[i]==nums[i+1])
            en++;
            else 
            break;
        }
        for(int i=pos;i>0;i--){
            if(nums[i]==nums[i-1])
            star--;
            else 
            break;
        }
        }
        temp.push_back(star);
        temp.push_back(en);

       
    return temp;}
};