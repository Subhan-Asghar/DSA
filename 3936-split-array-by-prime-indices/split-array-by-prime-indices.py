class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n=len(nums)
        def findPrimes(n):
            if n < 2:
                return []
            sieve = [True] * (n + 1)
            sieve[0] = sieve[1] = False  
        
            for i in range(2, int(n**0.5) + 1):
                if sieve[i]:
                    for j in range(i * i, n + 1, i):
                        sieve[j] = False

        
            primes = [i for i, is_prime in enumerate(sieve) if is_prime]
            return primes
        prime=set(findPrimes(n))
        sum_prime=0
        sum_other=0
        for i in range(n):
            if i in prime:
                sum_prime+=nums[i]
            else:
                sum_other+=nums[i]
        return abs(sum_prime-sum_other)
