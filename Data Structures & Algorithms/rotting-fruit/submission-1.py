class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = set()
        visited = set()
        agenda = deque()

        def add_rot(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited or grid[r][c] == 0):
                return
            agenda.append((r, c))
            visited.add((r, c))
            fresh.remove((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                if grid[r][c] == 2:
                    agenda.append((r, c))
                    visited.add((r, c))
        minutes = 0
        if not fresh:
            return minutes
        while agenda:
            for i in range(len(agenda)):
                r, c = agenda.popleft()
                add_rot(r + 1, c)
                add_rot(r - 1, c)
                add_rot(r, c + 1)
                add_rot(r, c - 1)
            minutes += 1
            if not fresh:
                return minutes
        return -1
            