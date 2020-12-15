import random

from sympy import *


def isPrime(x):
    count = 0
    for i in range(int(x / 2)):
        if x % (i + 1) == 0:
            count = count + 1
    return count == 1


# gives list of n primes starting from the K-th prime to L-th
def Random_n_Prime(k, l):
    numbers = [i for i in range(k, l + 1)]
    n_primes = []
    for i in range(l):
        rand = random.choice(numbers)
        n_primes.append(prime(rand))
        numbers.remove(rand)

    return n_primes


def Random_generators(n):
    numbers = [i for i in range(1, n + 1)]
    # chose one random prim from primes to find generator for it and return the generator
    n = prime(random.choice(numbers))
    s = set(range(1, n))
    results = []
    for a in s:
        g = set()
        for x in s:
            g.add((a ** x) % n)
        if g == s:
            results.append(a)
    # print(results)
    return random.choice(results)


def getRandom(greatestElement):
    systemRandom = random.SystemRandom()
    randomNumber = systemRandom.randint(1, greatestElement)
    return randomNumber


def prf(greatestIndex):
    """
    TODO
    what should be the universeSize ?

    prf function returns the Universes U as a list

    seed will be the size limit of the set of primes
    """
    size = getRandom(greatestIndex)
    res = []
    size += 1
    for i in range(1, size):
        tmp = getRandom(greatestIndex)
        tmpP = prime(tmp)
        if tmpP not in res:
            res.append(tmpP)
        else:
            size += 1
    return res


def getRandomFromList(l):
    return l[getRandom(len(l)) - 1]


def generat_crs(N, l):
    g = Random_generators(N)
    distinct_Primes = prf(l)
    crs = str(N) + ' ' + str(g)
    for i in range(0, len(distinct_Primes)):
        crs = crs + ' ' + str(distinct_Primes[i])

    return crs


def test_generator(g, number, size):
    l = {0}
    for i in range(size):
        l.add(g ** i % number)
    print(l)
