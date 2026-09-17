class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        res = 0

        while i < j:
            area = (j-i) * min(heights[i], heights[j])
            res = max(area, res)
            if heights[j] <= heights[i]: 
                j-=1
            else: 
                i += 1
            
        return res




        