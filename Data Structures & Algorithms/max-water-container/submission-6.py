class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i = 0
        j = len(heights) - 1
        while i != j:
            area = max(area, self.Area(i, j, heights[i], heights[j]))
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return area
    def Area(self, idx, idx2, h_1, h_2):    
        return (idx2 - idx) * (min(h_1, h_2))