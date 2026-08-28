class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out = float('-inf')
        curMax = float('-inf')
        for i in range(len(nums)):
            curMax = max(nums[i], curMax + nums[i])
            out = max(out, curMax)
        return out