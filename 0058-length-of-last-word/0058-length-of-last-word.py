class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a=s.split()
        l=a[-1]
        return len(l)