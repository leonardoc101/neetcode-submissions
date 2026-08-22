import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        out = []
        distances = [(math.sqrt(point[0]**2 + point[1]**2), i) for i, point in enumerate(points)]
        heapq.heapify(distances)
        for _ in range(k):
            out.append(points[heapq.heappop(distances)[1]])
        return out