class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        dp = [-1] * len(graph)
        def dfs(node):
            if dp[node] != -1:
                return dp[node]
            if len(graph[node]) == 0:
                dp[node] = True
                return True
            dp[node] = False
            is_safe_node = True
            for next_node in graph[node]:
                is_safe_node = is_safe_node and dfs(next_node)
            dp[node] = is_safe_node
            return dp[node]
        ans = []
        for i in range(len(graph)):
            dfs(i)
            if dp[i]:
                ans.append(i)
        return ans