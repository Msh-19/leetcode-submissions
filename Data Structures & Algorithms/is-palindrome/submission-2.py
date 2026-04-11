class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(c.lower() for c in s if self.alphaNum(c))

        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left +=1
            right -= 1
        return True
    
    def alphaNum(self,c):
        return (ord("A")<= ord(c) <= ord("Z") or 
        ord("a")<= ord(c) <= ord("z") or
        ord("0")<= ord(c) <= ord("9"))