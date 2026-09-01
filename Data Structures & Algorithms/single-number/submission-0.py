class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        out = 0
        for num in nums:
            out = num ^ out 
        return out