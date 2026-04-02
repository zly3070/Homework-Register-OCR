def linear_sieve(n):
    is_prime = [True] * (n + 1)
    primes = []
    
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        
        for p in primes:
            if i * p > n:
                break
            is_prime[i * p] = False
            if i % p == 0:
                break
    
    return primes

if __name__ == "__main__":
    n = int(input())
    primes = linear_sieve(n)
    print(' '.join(map(str, primes)))