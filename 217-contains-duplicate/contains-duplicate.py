class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if len(set(nums)) != len(nums):
        #     return True
        # return False
        freq_map =  {} # empty dictionary to store freqency
        for num in nums:
            freq_map[num] = freq_map.get(num,0)+1 #python dictionary concept to store freq
            if freq_map[num]>1:# Checking for duplicate
                return True
            
        return False
        

        