class Solution:
    def countPrimes(self, n: int) -> int:
        """
        def is_prime(k):
            if k == 2 or k == 3: return True
            if k % 2 == 0 or k < 2: return False
            for i in range(3, int(k ** 0.5) + 1, 2):
                if k % i == 0:
                    return False

            return True
        c = 0

        for i in range(n):
            if is_prime(i):
                c += 1
        return c
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)