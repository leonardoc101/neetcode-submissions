class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False


        left = 0
        right = len(s1)
        while right <= len(s2):
            if self.isAnagram(s1, s2[left:right]):
                return True
            else:
                right += 1
                left += 1
        return False

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
