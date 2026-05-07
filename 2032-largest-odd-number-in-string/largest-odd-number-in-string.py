class Solution:
    def largestOddNumber(self, num: str) -> str:
        nums=len(num)-1
        for i in range(nums,-1,-1):
            if int(num[i])%2!=0:
                return num[:i+1]
        return ""

        