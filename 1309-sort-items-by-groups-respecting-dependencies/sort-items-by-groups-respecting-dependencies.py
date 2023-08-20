from collections import defaultdict

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        res = []
        graph = [[] for _ in range(n + m)]
        indegree = [0] * (n + m)
        
        for i in range(n + m):
            graph[i] = []
        
        for i in range(len(group)):
            if group[i] == -1:
                continue
            graph[n + group[i]].append(i)
            indegree[i] += 1
        
        for i in range(len(beforeItems)):
            for item in beforeItems[i]:
                repBeforeItem = item if group[item] == -1 else n + group[item]
                repCurrentItem = i if group[i] == -1 else n + group[i]
                
                if repBeforeItem == repCurrentItem:
                    graph[item].append(i)
                    indegree[i] += 1
                else:
                    graph[repBeforeItem].append(repCurrentItem)
                    indegree[repCurrentItem] += 1
        
        for i in range(n + m):
            if indegree[i] == 0:
                self.dfs(graph, indegree, i, n, res)
        
        return res if len(res) == n else []

    def dfs(self, graph, indegree, cur, n, res):
        if cur < n:
            res.append(cur)
        indegree[cur] -= 1
        
        for child in graph[cur]:
            indegree[child] -= 1
            if indegree[child] == 0:
                self.dfs(graph, indegree, child, n, res)