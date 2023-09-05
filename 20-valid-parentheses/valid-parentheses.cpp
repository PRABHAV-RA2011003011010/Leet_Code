class Solution {
public:
    bool isValid(string s) {
        vector <char> ch;
        signed int top=-1;
        if(s.length()==1 || s[0]==')' || s[0]==']' || s[0]=='}' )
        return false;
        else{
        for(int i=0;i<s.length();i++){
            if(s[i]=='(' || s[i]=='[' || s[i]=='{' ){
                top++;
                ch.push_back(s[i]);
               
                
                }
            else if(!ch.empty()){
             if(s[i]==')' && ch[top]=='('){
                ch.pop_back();
                top--;

            }
            else if(s[i]=='}' && ch[top]=='{'){
                ch.pop_back();
                top--;

            }
            else if(s[i]==']' && ch[top]=='['){
                ch.pop_back();
                top--;

            }
            else return false;
            }
          else return false;  
            


        }
        }
        
    return top==-1?true:false;}
};