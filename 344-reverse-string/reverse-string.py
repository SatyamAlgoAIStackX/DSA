class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Here two pointer technique is used and swapping
        left = 0
        right = len(s)-1
        while(left<right):
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        