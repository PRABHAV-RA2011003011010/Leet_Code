class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> ch;
        int left=0,count=0;
        for(int right=0;right<s.size();right++){
            if(ch.count(s[right])==0){
                ch.insert(s[right]);
                count=max(count,right-left+1);

            }
            

            else{
            while(ch.count(s[right])){
                ch.erase(s[left]);
                left++;

            }
            ch.insert(s[right]);

            }

        }
        
    return count;}
};