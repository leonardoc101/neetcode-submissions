class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        l_idx = 0
        h_idx = n // 2 if n // 2 > 0 else 1


        while True:
            # check left and right for rift
            if nums[h_idx - 1] > nums[h_idx]:
                return nums[h_idx]
            if nums[(h_idx + 1) % n] < nums[h_idx]:
                return nums[(h_idx + 1) % n]

            # rift occurs in first half
            if nums[l_idx] > nums[h_idx]:
                if ((h_idx - l_idx) // 2) < 1:
                    h_idx = max(h_idx - 1, 0)
                    continue
                h_idx = h_idx - ((h_idx - l_idx) // 2)
            # rift occurs in second half
            else:
                l_idx = h_idx
                if ((h_idx - l_idx) // 2) < 1:
                    h_idx = min(h_idx + 1, n - 1)
                    continue
                h_idx = h_idx + ((h_idx - l_idx) // 2)
            