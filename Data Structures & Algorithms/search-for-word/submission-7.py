class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        max_r = len(board)
        max_c = len(board[0])
        out = False
        for r in range(max_r):
            for c in range(max_c):
                if board[r][c] == word[0]:
                    out = self.bfs_search(board, word, r, c, max_r, max_c)
                if out:
                    return True
        return out
    
    def bfs_search(self, board, word, r, c, max_r, max_c):
        agenda = deque()
        agenda.append(("", r, c, frozenset({(r, c)})))

        while agenda:
            cur, row, col, visited = agenda.popleft()
            if board[row][col] != word[len(cur)]:
                continue
            if cur + board[row][col] == word:
                return True
            for i in [-1, 1]:
                if 0 <= row + i < max_r:
                    if (row + i, col) not in visited:
                        agenda.append((cur + board[row][col], row + i, col, visited | {(row + i, col)}))
                if 0 <= col + i < max_c:
                    if (row, col + i) not in visited:
                        agenda.append((cur + board[row][col], row, col + i, visited | {(row, col + i)}))
        return False
