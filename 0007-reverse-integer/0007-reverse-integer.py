class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        n=""
        for i in range(len(s)):
            if s[i]=='-':
                continue
            n=s[i]+n
        b=int(n)
        if x<0:
            b = (-1)*b

        if b < -2147483648 or b > 2147483647:
            return 0

        return b