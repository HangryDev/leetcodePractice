class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        maxn = 2**31
        neg = False
        if x < 0:
            neg = True
        while x != 0:
            d = abs(x) % 10
            if rev > (maxn -1 - d)//10 or (rev > (maxn - d)//10 and neg):
                return 0
            rev = int(rev * 10 + d)
            x = int(x/10)
        if neg:
            rev = rev *-1
        return rev