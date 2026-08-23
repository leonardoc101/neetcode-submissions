class MedianFinder:

    def __init__(self):
        self.maxHeap = [float("-inf")]
        self.minHeap = [float("inf")]

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == len(self.minHeap):
            if num >= self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
            elif num <= self.maxHeap[0]:
                heapq.heappush_max(self.maxHeap, num)
            else:
                heapq.heappush(self.minHeap, num)
        elif len(self.maxHeap) > len(self.minHeap):
            if num >= self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush_max(self.maxHeap, num)
                heapq.heappush(self.minHeap, heapq.heappop_max(self.maxHeap))
        else:
            if num <= self.maxHeap[0]:
                heapq.heappush_max(self.maxHeap, num)
            else:
                heapq.heappush(self.minHeap, num)
                heapq.heappush_max(self.maxHeap, heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + self.maxHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return self.maxHeap[0]
        
        