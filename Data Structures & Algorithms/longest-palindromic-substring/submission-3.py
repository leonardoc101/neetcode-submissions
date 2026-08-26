class Solution:
    def longestPalindrome(self, s: str) -> str:
        outIdx, outLen = 0, 0 
        def pal(l, r):
            nonlocal outLen
            nonlocal outIdx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > outLen:
                    outLen = r - l + 1
                    outIdx = l
                l -= 1
                r += 1

        for i in range(len(s)):
            pal(i, i)
            pal(i, i + 1)

        return s[outIdx : outIdx + outLen]  
