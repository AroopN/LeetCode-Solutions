class Solution:
    def numSub(self, s: str) -> int:
        l = [int(i) for i in s]
        res = 0
        i = 0
        while i < len(l):
            if l[i] != 1:
                i += 1
                continue
            count = 0
            curr = 0
            while i < len(l) and l[i] == 1:
                i += 1
                count += 1
                curr += count
            res += curr
            res %= 10**9+7
        return res
