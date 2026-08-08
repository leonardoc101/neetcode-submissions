class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mid = int(n / 2)
        low = 0
        high = len(nums) - 1
        out = -1
        while low <= high:
            if nums[mid] > target:
                high = mid - 1
                mid = int((low + high) / 2)
            elif nums[mid] < target:
                low = mid + 1
                mid = int((low + high) / 2)
            else:
                out = mid
                break
        return out