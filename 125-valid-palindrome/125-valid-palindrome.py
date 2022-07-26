class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s.lower())
        return s==s[::-1]
        # i=0
        # j=len(s)-1
        # while i<=j:
        #     if s[i]!=s[j]:
        #         return False
        #     i+=1
        #     j-=1
        # return True
        