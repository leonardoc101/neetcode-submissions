class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:     
        connected = 0
        nodes = {i for i in range(n)}
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def bfs(node):
            agenda = deque([(node, -1)])
            while agenda:
                node, parent = agenda.popleft()
                for nei in adj[node]:
                    if nei == parent or nei not in nodes:
                        continue
                    nodes.remove(nei)
                    agenda.append((nei, node))
        
        while nodes:
            bfs(nodes.pop())
            connected += 1

        return connected