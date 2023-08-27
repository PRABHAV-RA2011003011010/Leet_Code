class Solution {
public:
    bool isPalindrome(int x) {
        long int temp=0;
        int reverse=x;
        if(x<0)
        return false;
        while(x){
            temp=temp*10+x%10;
            x=x/10;
        }
        if(reverse==temp)
        return true;
        
    return false;}
};