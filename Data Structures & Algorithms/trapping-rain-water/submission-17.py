class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        blocked = 0
        i = 0
        j = 1
        while i < len(height) - 1:
            max_idx = None
            max_b = 0
            max_h = 0
            blocked = 0
            no_right = False
            if height[i] == 0:
                i += 1
                j = i + 1
                continue
            while height[j] < height[i]:
                if height[j] > max_h:
                    max_h = height[j]
                    max_idx = j
                    max_b = blocked
                blocked += height[j]
                j += 1
                if j >= len(height):
                    no_right = True
                    break
            if no_right:
                if max_idx is None:
                    return water
                water += self.Area(i, max_idx, height[i], height[max_idx]) - max_b
                i = max_idx
                no_right = False
            else:
                water += self.Area(i, j, height[i], height[j]) - blocked
                i = j
            max_b = 0
            blocked = 0
            j = i + 1
        return water
    def Area(self, idx, idx2, h_1, h_2):    
        return (idx2 - idx - 1) * (min(h_1, h_2))