class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Imports
        from collections import defaultdict
        import heapq
        # Constructing graph
        graph = defaultdict(list)
        for i, edge in enumerate(edges):
            s, e = edge
            graph[s].append((e, succProb[i]))
            graph[e].append((s, succProb[i]))

        # Similar to Dijkstra's algorithm using max-heap
        heap = []
        for i in graph[start]:
            heapq.heappush(heap, (-i[1], i[0]))
        visited = set()
        while heap:
            curr = heapq.heappop(heap)
            if curr[1] in visited:
                continue
            visited.add(curr[1])
            if curr[1] == end:
                return -curr[0]
            for i in graph[curr[1]]:
                heapq.heappush(heap, (curr[0] * i[1], i[0]))
        return 0
