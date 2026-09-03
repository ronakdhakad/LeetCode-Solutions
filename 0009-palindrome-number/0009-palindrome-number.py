class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        reverse=""
        for i in range(0,len(y)):
            reverse=y[i]+reverse
        if y==reverse:
            return True
        else:
            return False
        