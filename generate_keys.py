import random

def generate_key():
    x = random.randrange(150, 300)
    y = random.randrange(x, 300)
    primes = get_primes(x, y)
    p, q = primes[0], primes[1]
    e = gen_rel_prime(p - 1, q - 1)
    d = pow(e, -1, ((p - 1) * (q - 1)))
    N = primes[0] * primes[1]
    return(d, (N, e))

def gen_rel_prime(x, y) :
    i = 2
    while True:
        if x % i != 0 and y % i != 0:
            return i
        i += 1

def generate_primes():
    primes = set()
    i = 2
    while True:
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(i)
            yield i
        i += 1

def get_primes(x, y):
    prime1 = 0
    prime2 = 0
    gen = generate_primes()
    for i in range(x):
        next(gen)
    prime1 = next(gen)
    for i in range(y - x):
        next(gen)
    prime2 = next(gen)
    return (prime1, prime2)
