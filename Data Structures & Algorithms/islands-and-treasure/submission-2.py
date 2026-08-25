class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        agenda = deque()

        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == -1):
                return
            visit.add((r, c))
            agenda.append([r, c])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    agenda.append([r, c])
                    visit.add((r, c))
        
        d = 0
        while agenda:
            for i in range(len(agenda)):
                r, c = agenda.popleft()
                grid[r][c] = d
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            d += 1