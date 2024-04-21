class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbours = {}
        for u,v in edges:
            if u in neighbours:
                neighbours[u].append(v)
            else:
                neighbours[u]=[v]
            if v in neighbours:
                neighbours[v].append(u)
            else:
                neighbours[v]=[u]
        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for neighbor in neighbours[node]:
                if neighbor not in visited:
                    if dfs(neighbor, visited):
                        return True
            return False
        
        visited = set()
        return dfs(source, visited)
        
        