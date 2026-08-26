class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        
        agenda = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                agenda.append(n)
        idx = 0
        ordering = []
        while agenda:
            node = agenda.popleft()
            ordering.append(node)
            idx += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    agenda.append(nei)
        if idx != numCourses:
            return []
        ordering.reverse()
        return ordering