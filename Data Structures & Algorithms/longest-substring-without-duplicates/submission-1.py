class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        left = 0
        res  = 0 

        for right in range(len(s)):
            if s[right] in dic:
                left = max(dic[s[right]]+1,left)
            dic[s[right]] = right
            res = max(res,right-left+1)
        return res