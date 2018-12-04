def seive_of_eratosthenes(n):
    # seive of eratosthenes algorithm,
    # n as the limit
    primes = [True for x in range(n+1)]
    primes[0], primes[1] = False, False

    i = 2
    while (i ** 2 < n):
        print("i", i)
        if primes[i]:
            j = i ** 2
            while (j <= n):
                primes[j] = False
                j += i
        i += 1

    for idx, elem in enumerate(primes):
        if elem:
            yield idx


for p in seive_of_eratosthenes(100):
    print(p)
