class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        left = 0
        right = 0
        freqMap = {}
        for char in s1:
            freqMap[char] = 1 + freqMap.get(char, 0)
        curMap = {}
        while right != len(s1):
            curMap[s2[right]] = 1 + curMap.get(s2[right], 0)
            right += 1
        if curMap == freqMap:
            return True

        while right < len(s2):
            curMap[s2[left]] -= 1
            if curMap[s2[left]] == 0:
                curMap.pop(s2[left])
            left += 1
            curMap[s2[right]] = 1 + curMap.get(s2[right], 0)
            right += 1
            if curMap == freqMap:
                return True
        return False
