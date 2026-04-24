class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=1:
            return 0
        #Make array of prime no. initially all no.is prime
        prime = [True]*(n)
        prime[0] = prime[1] = False # 0 and 1 is not prime
        
        #start from 2
        p=2
        while p*p<=n: # We have to check prime upto root n
            if prime[p]: #check prime
                for i in range(p*p, n, p): # multiple of prime = false
                    prime[i]=False
            p+=1
        count=0
        for i in range(2, n):
            if prime[i]:
                count+=1
        return count


