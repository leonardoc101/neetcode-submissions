class Solution:
    def countSubstrings(self, s: str) -> int:
        out = 0

        def pal(l, r):
            nonlocal out
            while l >= 0 and r < len(s) and s[l] == s[r]:
                out += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            pal(i, i)
            pal(i, i + 1)
        return out