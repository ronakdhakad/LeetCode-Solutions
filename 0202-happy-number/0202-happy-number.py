class Solution:
    def isHappy(self, n: int) -> bool:
        
        l=len(str(n))
        sum=0
        s=set()
        while(n!=1):
            if (n in s):
                return False

            s.add(n)
            while(n!=0):
                a=n%10
                n=n//10
                sum=sum+(a*a)

            n=sum
            sum=0
            if n==1:
                return True
        return True
    

        
