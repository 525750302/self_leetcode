class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parents[i]].append(i)
 
        geneSet = set()
        visited = [False] * n
        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            geneSet.add(nums[node])
            for child in children[node]:
                dfs(child)

        node = nums.index(1) if 1 in nums else -1
        res, iNode = [1] * n, 1

        while node != -1:
            dfs(node)
            while iNode in geneSet:
                iNode += 1
            res[node], node = iNode, parents[node]
        return res