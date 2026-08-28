class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # if (total % 2 != 0):
        #     return False
        target = total / 2

        def dfs(i, cur):
            if cur == target:
                return True
            if cur > target or i >= len(nums):
                return False
            return dfs(i + 1, cur + nums[i]) or dfs(i + 1, cur)

        return dfs(0, 0)
            
