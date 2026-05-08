class Solution:
    def secondHighest(self, s: str) -> int:
        first=second=-1
        for char in s:
            if char.isdigit():# extract digit from character
                d=int(char) # convert into int
                if d>first:
                    second = first
                    first = d
                elif second < d < first:
                    second = d
        return second
        