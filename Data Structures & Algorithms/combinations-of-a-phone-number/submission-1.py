class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        out = []
        dig_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def dfs(i, cur):
            if i >= len(digits):
                out.append(cur)
                return
            for char in dig_to_char[digits[i]]:
                dfs(i + 1, cur + char)
        dfs(0, "")
        return out

        