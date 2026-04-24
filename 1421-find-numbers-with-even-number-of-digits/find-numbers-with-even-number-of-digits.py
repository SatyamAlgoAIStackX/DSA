class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        num = nums
        countEven=0
        for i in range(0,len(nums)):

            count=0
            
            while (num[i]>0):
                digit=num[i]%10
                count+=1
                num[i]=num[i]//10
            
            if (count%2==0):
                countEven += 1
        return countEven
            
            
