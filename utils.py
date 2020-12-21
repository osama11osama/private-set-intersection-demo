import random

from sympy import *


def getRandom(greatestElement):
    systemRandom = random.SystemRandom()
    randomNumber = systemRandom.randint(1, greatestElement)
    return randomNumber


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def findGenerator(N):
    list = []
    for i in range(1, N):
        if gcd(N, i) == 1:
            list.append(i)
    return random.choice(list)


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
