# works for python before 3.14
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if largest == second:
                continue
            else:
                heapq.heappush(stones, -1 * (largest - second))
        if stones:
            return -stones[0]
        else:
            return 0