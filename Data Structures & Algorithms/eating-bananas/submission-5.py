import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        low = 0
        high = max(piles)
        mid = int((low + high) / 2)
        prev = 1
        while low <= high:
            if mid != 0:
                t = self.simulate(piles, mid)
            else:
                break
            if t > h:
                low = mid + 1
                mid = int((low + high) / 2)
            elif t < h:
                high = mid - 1
                prev = mid
                mid = int((low + high) / 2)
            else:
                high = mid - 1
                prev = mid
                mid = int((low + high) / 2)
        return prev
                
    def simulate(self, piles, rate):
        time = 0 
        for pile in piles:
            time += math.ceil(pile / rate)
        return time

