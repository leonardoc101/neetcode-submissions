class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s_nums = sorted(list(set(nums)))
        longest = []
        seq = [s_nums[0]]
        for i in range(len(s_nums) - 1):
            if (s_nums[i + 1] - s_nums[i]) != 1:
                if len(seq) > len(longest):
                    longest = seq.copy()
                seq = [s_nums[i + 1]]
                continue
            else:
                seq.append(s_nums[i + 1])
        if len(seq) > len(longest):
            longest = seq.copy()
        return len(longest)