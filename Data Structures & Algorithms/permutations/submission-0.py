class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        # base cases
        if len(nums) < 2:
            return [nums]
        if len(nums) == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        
        for i in range(len(nums)):
            first, rest = nums[i], [nums[j] for j in range(len(nums)) if j != i]
            without_first = self.permute(rest)
            starts_with_first = [[first] + subset for subset in without_first]
            out.extend(starts_with_first)
        return out
