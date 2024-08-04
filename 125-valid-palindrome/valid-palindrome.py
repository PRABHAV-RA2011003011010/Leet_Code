class Solution:
    def isPalindrome(self, s: str) -> bool:
        pali=""
        for i in s:
            if(i!=" " and i.isalnum()):
                pali=pali+i.lower()
        rev=pali[::-1]

        return True if rev==pali else False