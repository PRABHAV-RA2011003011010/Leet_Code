class Solution {
public:
    int singleNumber(vector<int>& nums) {
        map <int,int> a;int m;
        for(auto x:nums){
            a[x]++;
        }
        for(auto y:a){
            if(y.second==1){
                m=y.first;

            }
        }

    return m;}
};