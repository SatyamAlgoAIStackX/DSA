class Solution:
    def countDigits(self, num: int) -> int:
        nums = num
        count=0
        while nums>0:
            digit=nums%10
            if (num % digit==0):
                count+=1
            nums = int(nums/10)
        return count
