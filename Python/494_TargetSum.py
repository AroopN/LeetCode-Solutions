class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        nums.sort()
        from functools import lru_cache
        @lru_cache(None)
        def helper(index, curr):
            if index == len(nums):
                return 1 if curr == S else 0
            return helper(index+1, curr-nums[index]) + helper(index+1, curr+nums[index])
        return helper(0, 0)
