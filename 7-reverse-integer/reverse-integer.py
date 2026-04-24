class Solution:
    def reverse(self, x: int) -> int:
        num = x 
        res=0
        max_value=2**31-1
        min_value=-2**31
        sign=-1 if num<0 else 1
        num = abs(x)
        while (num!=0):
            last_digit=num%10
            if (res>max_value/10) or (res<min_value/10):
                return 0
            res = res*10+last_digit
            num=int(num/10)
        return res*sign
        