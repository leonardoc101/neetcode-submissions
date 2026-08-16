class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        first, rest = nums[0], nums[1:]
        without_first = self.subsets(rest)
        with_first = [[first] + subset for subset in without_first]
        return with_first + without_first