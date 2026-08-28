class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [False for _ in range(len(nums))]
        memo[-1] = True
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] == 0:
                continue
            for jump in range(nums[i], 0, -1):
                if (i + jump) >= n:
                    memo[i] = True
                    break
                if memo[i + jump]:
                    memo[i] = True
                    break
        return memo[0]