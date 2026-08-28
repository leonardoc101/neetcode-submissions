class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        out = float("-inf")
        curMax = float("-inf")
        idx = 0
        total = 0
        for i in range(len(gas)):
            delt = gas[i] - cost[i]
            total += delt
            if curMax + delt > delt:
                curMax = curMax + delt
            else:
                curMax = delt
                idx = i
            if curMax > out:
                out = curMax
        return idx if total >= 0 else -1

            