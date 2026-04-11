class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right = 0, len(heights)-1
        res = 0
        while left<right:
            w = right - left
            h = min(heights[left],heights[right])
            area = w*h
            res = max(res,area)
            if heights[left] <= heights[right]:
                left+=1
            else:
                right-=1
        return res
