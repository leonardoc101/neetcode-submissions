class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        while len(strs) != 0:
            word = strs.pop()
            sub_out = [word]
            i = 0
            while i < len(strs):
                if self.isAnagram(word, strs[i]):
                    sub_out.append(strs[i])
                    strs.remove(strs[i])
                else:
                    i += 1
            out.append(sub_out)
        return out

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_list = list(t)
        for char in s:
            try:
                t_list.remove(char)
            except ValueError:
                return False
        if len(t_list) == 0:
            return True
        return False