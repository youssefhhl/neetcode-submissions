class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        s=s.lower()
        i=0
        j=n-1
        while(i<j):
            if(s[i].isalnum() and s[j].isalnum() and s[i]!=s[j]):
                return False
            elif(not s[i].isalnum()):
                i+=1
            elif(not s[j].isalnum()):
                j-=1
            else:
                i+=1
                j-=1
        return True

