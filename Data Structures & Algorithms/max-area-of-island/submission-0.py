class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set() # (r, c) tuples
        count = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        ROWS = len(grid)
        COLS = len(grid[0])

        def cur_island(r, c):
            cur = 1
            agenda = deque()
            agenda.append((r, c))
            seen.add((r, c))

            while agenda:
                r, c = agenda.popleft()
                for d in directions:
                    new_cell = (r + d[0], c + d[1])
                    if new_cell in seen:
                        continue
                    if (0 <= new_cell[0] < ROWS) and (0 <= new_cell[1] < COLS) and (grid[new_cell[0]][new_cell[1]] == 1):    
                        agenda.append(new_cell)
                        seen.add(new_cell)
                        cur += 1  
            return cur

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in seen:
                    island_area = cur_island(r, c)
                    count = max(count, island_area)
        return count