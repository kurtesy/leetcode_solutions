class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        d = {}
        res = []
        cons = [tuple(i) for i in connections]
        for start, end in connections:
            if start in d:
                d[start] += [end]
            else:
                d[start] = [end]
            if end in d:
                d[end] += [start]
            else:
                d[end] = [start]
        for node in range(n):
            if len(d[node]) == 1:
                res.append([d[node][0],node])
            print(d[node])
        ans = []
        for i in res:
            if tuple(i) in cons:
                ans.append(i)
        return ans