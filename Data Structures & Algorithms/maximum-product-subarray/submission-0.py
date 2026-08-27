class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        out = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums:
            tmp = curMax * n
            curMax = max(n, n * curMax, n * curMin)
            curMin = min(n, tmp, n * curMin)
            out = max(out, curMax)
        return out