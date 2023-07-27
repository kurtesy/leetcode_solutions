class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)

        @functools.lru_cache(None)
        def dfs(cur, cur_fuel):
            if cur_fuel < 0:
                return 0
            temp = 0
            if cur == finish:
                temp += 1
            for i in range(n):
                if i == cur:
                    continue
                use_fuel = abs(locations[i] - locations[cur])
                temp += dfs(i, cur_fuel - use_fuel)
            return temp

        return dfs(start, fuel) % (10 ** 9 + 7)
