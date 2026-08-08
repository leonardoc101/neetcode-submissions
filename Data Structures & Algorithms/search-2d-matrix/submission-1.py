class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        mid = int(len(matrix) / 2)
        out = -1
        while low <= high:
            if matrix[mid][0] > target:
                high = mid - 1
                mid = int((low + high) / 2)
            elif matrix[mid][-1] < target:
                low = mid + 1
                mid = int((low + high) / 2)
            else:
                out = self.search(matrix[mid], target)
                break
        if out == -1:
            return False
        else:
            return True

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