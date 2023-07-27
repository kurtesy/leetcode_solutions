class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        graph = defaultdict(list)
        eq_to_val = {}
        for k, v in enumerate(equations):
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
            eq_to_val[(v[0],v[1])] = values[k]
            eq_to_val[(v[1],v[0])] = 1/values[k]
        ###do DFS or BFS for each query
        res = []
        for start, end in queries:
            if start not in graph or end not in graph:
                res.append(-1.0)
                continue
            stack = [(start, 1)]
            visited = set()
            while stack:
                curr, curr_prod = stack.pop()
                if curr==end:
                    res.append(curr_prod)
                    break
                if graph[curr]:
                    for nbor in graph[curr]:
                        if (curr, nbor) in visited: #avoid recomputing
                            continue
                        visited.add((curr, nbor))
                        stack.append((nbor, curr_prod*(eq_to_val[(curr, nbor)])))
            if curr!=end:
                res.append(-1.0)
        return res
        
            
        