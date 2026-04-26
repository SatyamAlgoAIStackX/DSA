class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        slow=0       #slow pointer
        
        for fast in range(1, len(nums)):   #fast pointer
        
            if nums[slow]!=nums[fast]:
                slow+=1
                nums[slow]=nums[fast]         
            
            
        return slow+1


        
        