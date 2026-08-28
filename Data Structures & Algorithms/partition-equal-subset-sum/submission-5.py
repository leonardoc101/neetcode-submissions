class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if (total % 2 != 0):
            return False
        target = int(total / 2)
        dp = {target: True}

        def dfs(i, cur):
            if cur in dp:
                return dp[cur]
            if cur > target or i >= len(nums):
                return False
            dp[cur] = dfs(i + 1, cur + nums[i]) or dfs(i + 1, cur)
            return dp[cur]

        return dfs(0, 0)