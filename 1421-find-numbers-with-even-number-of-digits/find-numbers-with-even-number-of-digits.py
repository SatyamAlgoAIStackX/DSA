class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        countEven=0
        for i in nums:
            if len(str(i)) % 2==0:
                countEven+=1

        return countEven
            
            
