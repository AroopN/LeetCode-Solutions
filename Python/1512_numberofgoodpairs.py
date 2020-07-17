class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        h = defaultdict(int)
        res = 0
        for i in nums:
            res += h[i]
            h[i] += 1
        return res
