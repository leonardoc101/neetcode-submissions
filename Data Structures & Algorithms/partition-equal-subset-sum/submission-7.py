class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if (total % 2 != 0):
            return False
        target = int(total / 2)
        dp = {}

        def dfs(i, cur):
            if cur == target:
                return True
            if cur > target or i >= len(nums):
                return False
            if (i, cur) in dp:
                return dp[(i, cur)]
            dp[(i, cur)] = dfs(i + 1, cur + nums[i]) or dfs(i + 1, cur)
            return dp[(i, cur)]

        return dfs(0, 0)