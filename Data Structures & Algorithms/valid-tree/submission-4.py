class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for i in range(n)]
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        agenda = deque([(0, - 1)])
        visited.add(0)

        while agenda:
            node, parent = agenda.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                visited.add(nei)
                agenda.append((nei, node))
        
        return len(visited) == n
        