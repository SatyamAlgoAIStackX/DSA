class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq={}
        #frequency count
        for i in nums:
            freq[i]=freq.get(i,0)+1
        #max freq count
        mxfreq=0
        for frq in freq.values():
            mxfreq=max(mxfreq,frq)
        #total freq count of max count
        totalfreq=0
        for frq in freq.values():
            if frq==mxfreq:
                totalfreq+=frq
        return totalfreq

        
        