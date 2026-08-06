class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        longest = ""
        cur = s[0]
        i = 1
        while i < len(s):
            if s[i] not in cur:
                cur += s[i]
            else:
                if len(cur) > len(longest):
                    longest = cur
                while s[i] in cur:
                    cur = cur[1:]
                cur += s[i]
            i += 1
        if len(cur) > len(longest):
            longest = cur
        return len(longest)