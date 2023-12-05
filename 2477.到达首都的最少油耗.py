class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        g = [[] for i in range(len(roads) + 1)]
        for e in roads:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        res = 0
        def dfs(cur, fa):
            nonlocal res
            peopleSum = 1 
            for ne in g[cur]:
                if ne != fa:
                    peopleCnt = dfs(ne, cur)
                    peopleSum += peopleCnt
                    res += (peopleCnt + seats - 1) // seats
            return peopleSum
        dfs(0, -1)
        return res

