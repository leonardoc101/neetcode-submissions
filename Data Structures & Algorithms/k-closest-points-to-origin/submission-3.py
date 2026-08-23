class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            dist = (x ** 2 + y ** 2)
            heapq.heappush_max(maxHeap, [dist, x ,y])
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)
        out = []
        while maxHeap:
            dist, x, y = heapq.heappop_max(maxHeap)
            out.append([x, y])
        return out