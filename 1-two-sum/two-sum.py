class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hash={}
        for i,num in enumerate(nums):#here i indicates index and num indicates its value
            complement=target-num
            if complement in Hash:
                return [Hash[complement],i]
            Hash[num]=i
        return []
        
        
            
        



        