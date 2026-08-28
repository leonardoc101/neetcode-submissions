class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        delta = []
        total = 0
        for i in range(len(gas)):
            cur_d = gas[i] - cost[i]
            delta.append(cur_d)
            total += cur_d
        if total < 0:
            return -1

        def find_idx(delt):
            out = float("-inf")
            curMax = float("-inf")
            idx = 0

            for i in range(len(delt)):
                if curMax + delt[i] > delt[i]:
                    curMax = curMax + delt[i]
                else:
                    curMax = delt[i]
                    idx = i
                if curMax > out:
                    out = curMax
            return idx
        return find_idx(delta)
            
        
        