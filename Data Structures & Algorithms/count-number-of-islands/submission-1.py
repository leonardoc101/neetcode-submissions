class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set() # (r, c) tuples
        count = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0])

        def add_island(r, c):
            agenda = deque()
            agenda.append((r, c))
            
            while agenda:
                r, c = agenda.popleft()
                for d in directions:
                    new_cell = (r + d[0], c + d[1])
                    if new_cell in seen:
                        continue
                    if (0 <= new_cell[0] < ROWS) and (0 <= new_cell[1] < COLS) and (grid[new_cell[0]][new_cell[1]] == "1"):    
                        agenda.append(new_cell)
                        seen.add(new_cell)    

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    count += 1
                    add_island(r, c)
        return count
