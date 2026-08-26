class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return true

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(cur, prev):
            if cur in visited:
                return False
            
            visited.add(cur)
            for nei in adj[cur]:
                if nei == prev:
                    continue
                if not dfs(nei, cur):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n
