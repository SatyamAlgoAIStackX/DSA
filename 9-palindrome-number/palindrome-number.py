class Solution:
    def isPalindrome(self, x: int) -> bool:
        # here extraction of nuber is used
        nums = x 
        res = 0
        while (nums>0):
            digit=nums%10
            res = (res*10) + digit
            nums = nums//10
        return res==x