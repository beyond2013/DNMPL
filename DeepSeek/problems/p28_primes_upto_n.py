"""Problem 28: All primes up to N (Sieve of Eratosthenes)."""
n = int(input("N: "))
sieve = [True]*(n+1)
sieve[0:2] = [False, False]
for i in range(2, int(n**0.5)+1):
    if sieve[i]:
        for j in range(i*i, n+1, i):
            sieve[j] = False
print([i for i in range(n+1) if sieve[i]])
