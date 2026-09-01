class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        for i in range(32):
            if (1 << i) & n:
                out += 1
        return out