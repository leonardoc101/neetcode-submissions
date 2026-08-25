class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        edges = set()
        for r in range(ROWS):
            edges.add((r, 0))
            edges.add((r, COLS - 1))
        for c in range(COLS):
            edges.add((0, c))
            edges.add((ROWS - 1, c))

        def check_and_surround(r, c):
            region = {(r, c)}
            agenda = deque()
            agenda.append((r, c))
            visited.add((r, c))
            while agenda:
                r, c = agenda.popleft()
                for dr, dc in directions:
                    new_cell = (r + dr, c + dc)
                    if (0 <= new_cell[0] < ROWS) and (0 <= new_cell[1] < COLS) and (new_cell not in visited) and (board[new_cell[0]][new_cell[1]] == "O"):    
                        agenda.append(new_cell)
                        visited.add(new_cell)
                        region.add(new_cell)
            if not (edges & region):
                for r, c in region:
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visited:
                    check_and_surround(r, c)