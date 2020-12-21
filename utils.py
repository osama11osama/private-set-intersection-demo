import random
from sympy import *
from Crypto.Hash import HMAC, SHA256


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


def prf(secretKey, elementsSet):
    res = []
    secretKeyByte = str(secretKey).encode('utf-8')
    HMac = HMAC.new(secretKeyByte, digestmod=SHA256)
    for i in elementsSet:
        element = str(i).encode('utf-8')
        HMac.update(element)
        pr = nextprime(int(HMac.hexdigest(), 16))
        res.append(pr)
    return res


def generate_crs(N, l):
    g = findGenerator(N)
    distinct_Primes = prf(l)
    crs = str(N) + ' ' + str(g)
    for i in range(0, len(distinct_Primes)):
        crs = crs + ' ' + str(distinct_Primes[i])

    return crs
