class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=str(n)
        sol=0
        for i in range(len(s)):
            if(i%2==0):
                sol+=int(s[i])
            else:
                sol-=int(s[i])
        
        return sol

        