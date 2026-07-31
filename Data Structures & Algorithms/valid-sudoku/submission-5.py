class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sud_dict = {
            "1" : [[], []],
            "2" : [[], []],
            "3" : [[], []],
            "4" : [[], []],
            "5" : [[], []],
            "6" : [[], []],
            "7" : [[], []],
            "8" : [[], []],
            "9" : [[], []],
        }
        square_dict = {
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            4 : [],
            5 : [],
            6 : [],
            7 : [],
            8 : [],
        }
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                if board[r][c] not in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                    return False
                sud_dict[board[r][c]][0].append(r)
                sud_dict[board[r][c]][1].append(c)
                square_dict[int(int(int(r) / 3) * 3 + int(int(c) / 3))].append(board[r][c])
        for key in sud_dict:
            if (self.hasDuplicate(sud_dict[key][0]) 
            or  self.hasDuplicate(sud_dict[key][1])):
                return False
        for k in square_dict:
            if self.hasDuplicate(square_dict[k]):
                return False
        return True

    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False