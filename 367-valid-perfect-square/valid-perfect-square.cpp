class Solution {
public:
    bool isPerfectSquare(int num) {
        int long sum=1,t=1;
        while(num>=sum){
            if(sum==num){
                return true;
            }
            sum=t*t;
            t++;

        }
        
    return false;}
};