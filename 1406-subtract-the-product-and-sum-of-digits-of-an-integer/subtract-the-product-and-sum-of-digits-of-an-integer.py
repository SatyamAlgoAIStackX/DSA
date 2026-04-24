class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = n
        sum_=0
        prod = 1
        while (nums>0):
            digit=nums%10
            prod *= digit
            sum_ += digit
            nums = nums//10
        return prod-sum_
