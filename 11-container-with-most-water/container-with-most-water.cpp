class Solution {
public:
    int maxArea(vector<int>& height) {
        int max1=0,temp;
        int left=0,right=height.size()-1;
        while(right>left){
            temp=min(height[right],height[left])*(right-left);
            max1=max(max1,temp);
            if(height[right]>height[left])
                left++;
            else
                right--;
            
        }


       

        
        
    return max1;}
};