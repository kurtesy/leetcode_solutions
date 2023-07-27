class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for u,v,w in times:
            if u in graph:
                graph[u] += [[v,w]]
            else:
                graph[u] = [[v,w]]
        self.n = n
        self.ans = 0
        self.queue = [k]
        if k not in graph:
            return -1
        self.dfs(graph, k)
        print(self.queue)
        return self.ans
        
    def dfs(self, graph, start):
        self.n-=1
        if start not in graph:
            return
        if self.n > 0:
            conn = graph[start]
            curMax = 0
            for c in conn:
                curMax = max(curMax, c[1])
                self.queue.append(c[0])
                self.dfs(graph, c[0])
            self.ans+=curMax
                
        