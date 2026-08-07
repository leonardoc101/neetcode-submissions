class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_a = 0
        seen = set()
        for i in range(len(heights)):
            cur_a = heights[i]
            j = i 
            if heights[i] == 0:
                continue
            if i > 0 and heights[i] == heights[i - 1]:
                continue
            while j > 0 and heights[j - 1] >= heights[i]:
                cur_a += heights[i]
                j -= 1
            try: 
                j = i
                while heights[j + 1] >= heights[i]:
                    cur_a += heights[i]
                    j += 1
            except IndexError:
                pass
            largest_a = max(largest_a, cur_a)
        return largest_a
